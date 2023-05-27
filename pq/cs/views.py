
# cs home view
from django.shortcuts import render, redirect
from django.db import connection
from django.db.models import Count
from datetime import datetime, timedelta
# Create your views here.
from django.views.generic import ListView
from django.views.generic import DetailView
from .models import cs, CSApproved, csqc, coilprocess, CSPI
from sa.models import sa
from set.models import cust
from django.db import transaction
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
import django_filters
# from myapp.models import cs

from django.views.generic import TemplateView
from django_filters.views import FilterMixin
# from .filters import CSFilter

from django.contrib.auth.models import User
from django.shortcuts import render
from .filters import UserFilter, CSFilter, CPFilter
from django_filters.views import FilterView
# from django.core.paginator import Paginator
from django.forms.models import inlineformset_factory
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .forms import CSUpdateForm,CSQCInlineFormSet, CSListEditForm, ImageFormSet, ChildrenFormset, CSAprInlineFormSet, CSCoilProInlineFormSet, CSCustProInlineFormSet, CSPIInlineFormSet
from django.forms import formset_factory, modelformset_factory
from django.contrib import messages
from .resources import CSResource
from .models import cs, CSApproved, Parent, pipegrade, custprocess
from tablib import Dataset
from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import date


from django.http import HttpResponse
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, Frame
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.colors import Color
from reportlab.graphics.shapes import Rect
from io import BytesIO
from django.utils import timezone

# def adblockcheck(request):
#     return render(request, 'cs/4-block-ad-block.html')

class CPFilter(LoginRequiredMixin, FilterView):
    filterset_class = CPFilter
    paginate_by = 10
    model = coilprocess
    template_name = 'cs/cp_filter.html'

class CSHome(LoginRequiredMixin, FilterView):
    filterset_class = CSFilter
    paginate_by = 10
    model = cs
    template_name = 'cs/cs_filter.html'
    # context_object_name = 'css'

    def get_queryset(self):
        # cursor = connection.cursor()
        # try:
        #     cursor.execute('EXEC [dbo].[get_pipegrade]')
        #     cursor.execute('EXEC [dbo].[get_coilgrade]')
        #     cursor.execute('EXEC [dbo].[get_cust]')
        #     cursor.execute('EXEC [dbo].[get_cs]')
        #     # result_set = cursor.fetchall()
        # finally:
        #     cursor.close()


        queryset = super().get_queryset()
        # queryset = cs.union()
        # Customize the queryset here
        # queryset = queryset[:100]
        # return queryset.filter(is_active=True)
        return queryset.order_by('-CSNo')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['coilpros'] = coilprocess.objects.filter(CSNo__in=self.object_list)
        # context['coilpros'] = coilprocess.objects.filter(CSNo=self.object.CSNo)
        return context

class CSUpdateView(LoginRequiredMixin, UpdateView):
    model = cs
    # fields = '__all__'
    form_class = CSUpdateForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        group_names = self.request.user.groups.values_list('name', flat=True)
        kwargs['group_names'] = group_names
        return kwargs
    
    def get_success_url(self):
        
        data = self.form.cleaned_data
        # return reverse_lazy('cs-update', kwargs={'pk': self.object.pk})
        sne_cs = self.request.POST.get('save-edit-cs')
        snp_cs = self.request.POST.get('save-print-cs')
        sne_sa = self.request.POST.get('save-edit-sa')
        snverup_cs = self.request.POST.get('save-upver-cs') # Save n version up - Upgrade version
        # sna_sa = self.request.POST.get('save-add-sa')   # Save n add new sa


        
        if data['GotoSAKey']:
            # return reverse_lazy('cs-detail', args=[data['GotoSAKey']])
            return reverse_lazy('sa-detail', kwargs={'pk': data['GotoSAKey']})
        
        if data['GotoCSKey'] :
            return reverse_lazy('cs-update', kwargs={'pk': data['GotoCSKey']})
        
        if sne_cs:
        #    return reverse('cs-update', args=(self.kwargs['pk'],))
           return reverse_lazy('cs-update', kwargs={'pk': self.object.pk})
        
        if snp_cs:
           return reverse_lazy('cs-detail', kwargs={'pk': self.object.pk})
        
        if sne_sa:
           if sa.objects.filter(SANo=self.object.SANo):
               return reverse_lazy('sa-update', kwargs={'pk': self.object.SANo}) 
           else:
               return reverse_lazy('sa-add', kwargs={'pk': self.object.SANo, 'cs': self.object.CSNo})     
        # if sna_sa:
        #    return reverse_lazy('sa-add', kwargs={'pk': self.object.SANo, 'cs': self.object.CSNo}) 
        
        if snverup_cs:
        #    return reverse('cs-add')
        #    return reverse_lazy('cs-add', kwargs={'pk':int(self.object.pk) + 1})
            return reverse_lazy('cs-add', kwargs={'pk': self.object.pk[:-2] + str(int(self.object.pk[-2:]) + 1).zfill(2)})


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context = super(CSUpdateView, self).get_context_data(**kwargs)
        # context['sa'] = self.kwargs.get('pk')
        context['pipegrades'] = pipegrade.objects.all()
        context['customers'] = cust.objects.all()
        context['sa_related_list'] = sa.objects.filter(SANo=self.object.SANo)
        context['pgrage_com_list'] = pipegrade.objects.filter(PipeGrade=self.object.PipeGrade_id)
        # context['cs'] = cs.objects.filter(SANo__in=self.object_list)
        context['coilpros'] = coilprocess.objects.filter(CSNo= self.kwargs.get('pk'))
        context['AppHistory'] = cs.objects.filter(CSNo__startswith=self.object.pk[:7]).order_by('-CSNo')

        if self.request.POST:
            context['CSApproved'] = CSAprInlineFormSet(self.request.POST, self.request.FILES, instance=self.object)
            context['CSCoilPro'] = CSCoilProInlineFormSet(self.request.POST, self.request.FILES, instance=self.object)
            context['CSCustPro'] = CSCustProInlineFormSet(self.request.POST, self.request.FILES, instance=self.object)

            context['CSPI'] = CSPIInlineFormSet(self.request.POST, self.request.FILES, instance=self.object)
            context['CSQC'] = CSQCInlineFormSet(self.request.POST, self.request.FILES, instance=self.object)

            
        else:
            context['CSApproved'] = CSAprInlineFormSet(instance=self.object)
            context['CSCoilPro'] = CSCoilProInlineFormSet(instance=self.object)
            context['CSCustPro'] = CSCustProInlineFormSet(instance=self.object)
            context['CSPI'] = CSPIInlineFormSet(instance=self.object)
            context['CSQC'] = CSQCInlineFormSet(instance=self.object)

        return context
    
    def form_valid(self, form):
        self.form = form
 
        context = self.get_context_data()
        
        CSAppr = context['CSApproved']
        CSCoilPro = context['CSCoilPro']
        CSCustPro = context['CSCustPro']
        CSPI = context['CSPI']
        CSQC = context['CSQC']

        messages.success(self.request, 'CS updated successfully at ' + timezone.localtime(timezone.now()).strftime("%Y-%m-%d %H:%M:%S"))

        with transaction.atomic():
            # Retrieve the model instance
            my_model = self.get_object()

            # Get the current value of the field
            current_value_DGDNote = my_model.DGDNote
            current_value_DGDJudgment = my_model.DGDJudgment

            current_value_ASManNote = my_model.ASManNote
            current_value_ASManJudgment = my_model.ASManJudgment

            current_value_PIManNote = my_model.PIManNote
            current_value_PIManJudgment = my_model.PIManJudgment

            current_value_QAManNote = my_model.QAManNote
            current_value_QAManJudgment = my_model.QAManJudgment

            current_value_QCManNote = my_model.QCManNote
            current_value_QCManJudgment = my_model.QCManJudgment

            current_value_PRManNote = my_model.PRManNote
            current_value_PRManJudgment = my_model.PRManJudgment

            current_value_PCManNote = my_model.PCManNote
            current_value_PCManJudgment = my_model.PCManJudgment
            
            # self.object = form.save(commit=False)
            if (current_value_DGDNote != form.cleaned_data['DGDNote']) or (current_value_DGDJudgment != form.cleaned_data['DGDJudgment']):
                
                # self define your field value
                self.object.DGDManDate = timezone.now()

            if (current_value_ASManNote != form.cleaned_data['ASManNote']) or (current_value_ASManJudgment != form.cleaned_data['ASManJudgment']):
                
                # self define your field value
                self.object.ASManDate = timezone.now()

            if (current_value_PIManNote != form.cleaned_data['PIManNote']) or (current_value_PIManJudgment != form.cleaned_data['PIManJudgment']):
                
                # self define your field value
                self.object.PIManDate = timezone.now()
            
            if (current_value_QAManNote != form.cleaned_data['QAManNote']) or (current_value_QAManJudgment != form.cleaned_data['QAManJudgment']):
                
                # self define your field value
                self.object.QAManDate = timezone.now()
            
            if (current_value_QCManNote != form.cleaned_data['QCManNote']) or (current_value_QCManJudgment != form.cleaned_data['QCManJudgment']):
                
                # self define your field value
                self.object.QCManDate = timezone.now()

            if (current_value_PRManNote != form.cleaned_data['PRManNote']) or (current_value_PRManJudgment != form.cleaned_data['PRManJudgment']):
                
                # self define your field value
                self.object.PRManDate = timezone.now()

            if (current_value_PCManNote != form.cleaned_data['PCManNote']) or (current_value_PCManJudgment != form.cleaned_data['PCManJudgment']):
                
                # self define your field value
                self.object.PCManDate = timezone.now()


            # Tracking editor
            self.object.LastUser = self.request.user.username
            self.object.LastimeUser = timezone.now()
            
            # self.object.LastUser = "Hung"

            self.object.save()

            # self.object = form.save()
            if CSCoilPro.is_valid() & CSCustPro.is_valid() & CSPI.is_valid() & CSQC.is_valid():
                
                CSCoilPro.instance = self.object
                CSCustPro.instance = self.object
                CSPI.instance = self.object
                CSQC.instance = self.object

                CSAppr.save()
                CSCoilPro.save()
                CSCustPro.save()

                CSPI.save()
                CSQC.save()

                

        return super().form_valid(form)

    # def save_form(self, form):
    #     # customize the save method to update a specific field
    #     instance = form.save(commit=False)
    #     # instance.field_to_update = form.cleaned_data['field_to_update']
    #     instance.PreBy = "timezone.get_current_timezone"
    #     instance.save()

    #    return instance
    # def save(self, commit=True):
    #     # get the value of field1
    #     SANo_value = self.request.POST.get('SANo')
        
    #     # your custom logic here
    #     return super().save(commit=commit)

class CSCreateView(LoginRequiredMixin, CreateView):
    model = cs
    # fields = '__all__'
    form_class = CSUpdateForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        group_names = self.request.user.groups.values_list('name', flat=True)
        kwargs['group_names'] = group_names
        return kwargs
    
    # Define initial values for the CSNo that upgraded
    def get_initial(self):
        initial = super().get_initial()
        if self.kwargs.get('pk') is not None:
            oldobj = cs.objects.get(CSNo = str(self.kwargs.get('pk')-1))
            # initial['CSNo'] = self.request.GET.get('pk')
            initial['CSNo'] = self.kwargs.get('pk')
            initial['OD'] = oldobj.OD
            initial['ID'] = oldobj.ID
            initial['WT'] = oldobj.WT
            initial['L'] = oldobj.L

            initial['AdjOD'] = oldobj.AdjOD
            initial['AdjID'] = oldobj.AdjID
            initial['AdjWT'] = oldobj.AdjWT
            initial['AdjL'] = oldobj.AdjL

            initial['PipeGrade'] = oldobj.PipeGrade

            initial['PreBy'] = self.request.user
            initial['CustID'] = oldobj.CustID
            initial['PackUnit'] = oldobj.PackUnit
            

            


        return initial
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context = super(CSUpdateView, self).get_context_data(**kwargs)
        # context['sa'] = self.kwargs.get('pk')
        context['pipegrades'] = pipegrade.objects.all()
        context['customers'] = cust.objects.all()

        return context
    
    def get_success_url(self):
        return reverse_lazy('cs-update', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        # Set the user field to the current user
        # form.instance.user = self.request.user

        # form.instance.IDate = date.today()
        # form.instance.DGDNote = None
        # form.instance.QCManNote = None
        # form.instance.QAManNote = None
        # form.instance.PIManNote = None
        # form.instance.PRManNote = None
        # form.instance.PCManNote = None
        # form.instance.ASManNote = None
        messages.success(self.request, 'CS created successfully at ' + timezone.localtime(timezone.now()).strftime("%Y-%m-%d %H:%M:%S"))
        # Call the parent class's form_valid() method to save the instance
        response = super().form_valid(form)

        # Perform any additional processing here

        return response
 
    
class CSDeleteView(LoginRequiredMixin, DeleteView):
    model = cs
    success_url = reverse_lazy('CSHome')

class CSDetailView(LoginRequiredMixin, DetailView):
    model = cs

    template_name = 'cs/cs_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['sa'] = self.kwargs.get('pk')
        context['csqc'] = csqc.objects.all().filter(CSNo = self.kwargs.get('pk'))[:1]
        context['coilpros'] = coilprocess.objects.all().filter(CSNo = self.kwargs.get('pk'))
        context['custpros'] = custprocess.objects.all().filter(CSNo = self.kwargs.get('pk'))
        context['CSPI'] = CSPI.objects.all().filter(CSNo = self.kwargs.get('pk'))
        return context

def cs_pdf(request, pk):
    # Retrieve the model instance from the database
    instance = cs.objects.get(pk=pk)

    # Create a file-like buffer to receive PDF data
    buffer = BytesIO()

    # Create a SimpleDocTemplate object
    doc = SimpleDocTemplate(buffer, 
                            pagesize=A4, 
                            title = 'Consideration Sheet', 
                            author='Heropoto',
                            subject='Waiting for approval',
                            keywords=['CS', pk])

    # Set the document margins in centimeters
    doc.leftMargin = 0.8 * cm
    doc.rightMargin = 0.8 * cm
    doc.topMargin = 0.8 * cm
    doc.bottomMargin = 0.8 * cm

    
    

    # Create a list of flowables to be added to the document
    elements = []

    

    # Add a title to the document
    title = Paragraph("Testing PDF Document", style=getSampleStyleSheet()["Title"])
    elements.append(title)

    # Add a title to the document
    title = "<h1>{}</h1>".format(instance.CSNo)
    elements.append(Paragraph(title, getSampleStyleSheet()["Title"]))

    # Add a paragraph to the document
    text = "<p>{}</p>".format(instance.SANo)
    elements.append(Paragraph(text, getSampleStyleSheet()["Normal"]))

    # Create a list of data for the table
    data = [['Name', 'Age', 'Gender'],
            ['XaKuTara', '25', 'Male'],
            ['Cutataxoa', '30', 'Female'],
            ['TaChoKuRa', '45', 'Male']]

    # Create a table style
    table_style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 14),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
        ('ALIGN', (0, 1), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 12),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        
    ])

    # Set the border style of the table
    # table_style.add('BOX', (0, 0), (-1, -1), 1, (0, 0, 0))  # Set outer border style
    # table_style.add('INNERGRID', (0, 0), (-1, -1), 0.5, (0, 0, 0))  # Set inner border style


    # Create a table object and apply the style
    table = Table(data)
    table.setStyle(table_style)

    # Add the table to the list of flowables
    elements.append(table)
    # # Create a new frame
    # frame = Frame(1*cm, 1*cm, width=10*cm, height=20*cm, showBoundary=1)
    # elements.append(frame)


    # Build the document
    doc.build(elements)

    # Get the value of the BytesIO buffer and create the response object
    pdf = buffer.getvalue()
    buffer.close()
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="{}.pdf"'.format(instance.CSNo)

    # Write the PDF to the response object
    response.write(pdf)
    return response



    


# class ParentList(ListView):
#     model = Parent
  
# class ParentCreate(CreateView):
#     model = Parent
#     fields = ['name']
#     success_url = reverse_lazy('parents-list')

#     def get_context_data(self):
#         context = super().get_context_data()
#         if self.request.POST:
#             context['children'] = ChildrenFormset(self.request.POST)
#         else:
#             context['children'] = ChildrenFormset()
#         return context
    
#     def form_valid(self, form):
#         context = self.get_context_data()
#         children = context['children']
#         with transaction.atomic():
#             self.object = form.save()
#             if children.is_valid():
#                 children.instance = self.object
#                 children.save()
#         return super().form_valid(form)








# BookFormSet = inlineformset_factory(cs, CSApproved, fields=('CSNo', 'CSAp'), extra=1)

# def CSEditView(request, cs_id):
#     author = cs.objects.get(CSNo = cs_id)
#     formset = BookFormSet(instance=author)
#     return render(request, 'cs_form.html', {'formset': formset})







# class CSInline():
#     form_class = CSUpdateForm
#     model = cs
#     template_name = "cs/create_or_update.html"

#     def form_valid(self, form):
#         named_formsets = self.get_named_formsets()
#         if not all((x.is_valid() for x in named_formsets.values())):
#             return self.render_to_response(self.get_context_data(form=form))

#         self.object = form.save()

#         # for every formset, attempt to find a specific formset save function
#         # otherwise, just save.
#         for name, formset in named_formsets.items():
#             formset_save_func = getattr(self, 'formset_{0}_valid'.format(name), None)
#             if formset_save_func is not None:
#                 formset_save_func(formset)
#             else:
#                 formset.save()
#         return redirect('CSHome')

   

#     def formset_images_valid(self, formset):
#         """
#         Hook for custom formset saving. Useful if you have multiple formsets
#         """
#         images = formset.save(commit=False)  # self.save_formset(formset, contact)
#         # add this 2 lines, if you have can_delete=True parameter 
#         # set in inlineformset_factory func
#         for obj in formset.deleted_objects:
#             obj.delete()
#         for image in images:
#             image.product = self.object
#             image.save()

# class CSCreate(CSInline, CreateView):

#     def get_context_data(self, **kwargs):
#         ctx = super(CSCreate, self).get_context_data(**kwargs)
#         ctx['named_formsets'] = self.get_named_formsets()
#         return ctx

#     def get_named_formsets(self):
#         if self.request.method == "GET":
#             return {
#                 # 'variants': VariantFormSet(prefix='variants'),
#                 'images': ImageFormSet(prefix='images'),
#             }
#         else:
#             return {
#                 # 'variants': VariantFormSet(self.request.POST or None, self.request.FILES or None, prefix='variants'),
#                 'images': ImageFormSet(self.request.POST or None, self.request.FILES or None, prefix='images'),
#             }


    
    




def CSListEditView(request):
    context ={}
  
    # creating a formset
    # CSFormSet = formset_factory(CSListEditForm, extra = 5 )
    CSFormSet = modelformset_factory(cs, fields =['CSNo'])
    
    formset = CSFormSet(request.POST or None)

    # print formset data if it is valid
    if formset.is_valid():
        for form in formset:
            print(form.cleaned_data)
    # Add the formset to context dictionary
    context['formset']= formset
    return render(request, "cs/cs_list_form.html", context)



def import_data(request):
    if request.method == 'POST':
        file_format = request.POST['file-format1']
        cs_resource = CSResource()
        dataset = Dataset()
        new_cs = request.FILES['importData']
        result =""
        if file_format == 'CSV':
            imported_data = dataset.load(new_cs.read().decode('utf-8'),format='csv')
            # Testing data import
            result = cs_resource.import_data(dataset, dry_run=True)                                                                 
        elif file_format == 'JSON':
            imported_data = dataset.load(new_cs.read().decode('utf-8'),format='json')
            # Testing data import
            result = cs_resource.import_data(dataset, dry_run=True) 
        elif file_format == 'XLS':
            imported_data = dataset.load(new_cs.read(),format='xls')
            # Testing data import
            result = cs_resource.import_data(dataset, dry_run=True) 
        if not result.has_errors():
            # Import now
            cs_resource.import_data(dataset, dry_run=False)
            messages.success(request, 'The file imported.')

    return render(request, 'cs/import_data.html')


def export_data(request):
    if request.method == 'POST':
        # Get selected option from form
        file_format = request.POST['file-format']
        cs_resource = CSResource()
        dataset = cs_resource.export()
        if file_format == 'CSV':
            response = HttpResponse(dataset.csv, content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="cs_exported_data.csv"'
            return response        
        elif file_format == 'JSON':
            response = HttpResponse(dataset.json, content_type='application/json')
            response['Content-Disposition'] = 'attachment; filename="cs_exported_data.json"'
            return response
        elif file_format == 'XLS (Excel)':
            response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
            response['Content-Disposition'] = 'attachment; filename="cs_exported_data.xls"'
            return response   
    return render(request, 'cs/export_data.html')






def search(request):
    user_list = User.objects.all()
    user_filter = UserFilter(request.GET, queryset=user_list)
    return render(request, 'search/user_list.html', {'filter': user_filter})



class CSListView(LoginRequiredMixin, ListView):
    model = cs
    # paginate_by = 10
    ordering = ['-LastimeUser']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['extral_field'] = 'Name of extral collum'
        return context

    def get_queryset(self):
        cursor = connection.cursor()
        try:
            cursor.execute('EXEC [dbo].[get_cs]')
            # result_set = cursor.fetchall()
        finally:
            cursor.close()
            
        today = datetime.today()
        three_months_ago = today - timedelta(days=90)
        queryset = super().get_queryset()
        # queryset = queryset.annotate(count=Count('CSNo'))
        return queryset.filter(LastimeUser__gte=three_months_ago)
    
