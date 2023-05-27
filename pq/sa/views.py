from django.shortcuts import render
from django.db import connection
from django.db.models import Count
from datetime import datetime, timedelta
# Create your views here.
from django.views.generic import ListView
from django.views.generic import DetailView
from django_filters.views import FilterMixin
from .models import sa
from set.models import EmailReport, surflevel
from cs.models import cs, coilprocess, csqc
import django_filters
from django.db.models import Q
from .forms import SASearchForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django_filters.views import FilterView
from .filters import SAFilter
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .forms import SAUpdateForm
from django.utils import timezone
from django.contrib import messages
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.urls import reverse

class SAHome(LoginRequiredMixin, FilterView):
    filterset_class = SAFilter
    paginate_by = 10
    model = sa
    template_name = 'sa/sa_filter.html'
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
        return queryset.order_by('-SANo')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cs'] = cs.objects.filter(SANo__in=self.object_list)
        context['coilpros'] = coilprocess.objects.filter(CSNo__in=context['cs'])
        # context['coilpros'] = coilprocess.objects.filter(CSNo__in=self.object_list)
        # context['coilpros'] = coilprocess.objects.filter(CSNo=self.object.CSNo)
        return context

class SACreateView(LoginRequiredMixin, CreateView):
    model = sa
    # fields = '__all__'
    form_class = SAUpdateForm

    def get_success_url(self):
        return reverse_lazy('sa-update', kwargs={'pk': self.object.pk})
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        group_names = self.request.user.groups.values_list('name', flat=True)
        kwargs['group_names'] = group_names
        return kwargs
    
    def get_initial(self):
        initial = super().get_initial()
        if self.kwargs.get('pk') is not None:
            csobj = cs.objects.get(CSNo = self.kwargs.get('cs'))
            # initial['CSNo'] = self.request.GET.get('pk')
            initial['SANo'] = self.kwargs.get('pk')
            initial['OD'] = csobj.OD
            initial['ID'] = csobj.ID
            initial['WT'] = csobj.WT
            initial['L'] = csobj.L

            

            initial['PipeGrade'] = csobj.PipeGrade

            initial['PreBy'] = self.request.user
            initial['CustID'] = csobj.CustID
            # initial['PackUnit'] = csobj.PackUnit
            initial['Model'] = csobj.Model
            initial['PartNo'] = csobj.PartNo
            initial['PartName'] = csobj.PartName
            initial['PartMaker'] = csobj.PartMaker

            initial['SKind'] = csobj.SKind
            initial['PKind'] = csobj.PKind
            initial['InBead'] = csobj.InBead

            initial['PackStd'] = (csobj.PackASNote or '')+ (csobj.PackPCNote or '')

            
            
            
            
        try: 
            csqcobj = csqc.objects.get(CSNo = self.kwargs.get('cs'))
            
            initial['AdjOD'] = csqcobj.AdjOD
            initial['AdjID'] = csqcobj.AdjID
            initial['AdjWT'] = csqcobj.AdjWT
            initial['AdjL'] = csqcobj.AdjL

            
            initial['TS'] = csqcobj.TS
            initial['YP'] = csqcobj.YP
            initial['EL'] = csqcobj.EL
            initial['Hardness'] = csqcobj.Hardness
            


            initial['ChC'] = csqcobj.ChC
            initial['ChSi'] = csqcobj.ChSi
            initial['ChMn'] = csqcobj.ChMn
            initial['ChP'] = csqcobj.ChP
            initial['ChS'] = csqcobj.ChS

            initial['ChAL'] = csqcobj.ChAL
            initial['ChNi'] = csqcobj.ChNi
            initial['ChCr'] = csqcobj.ChCr
            initial['CHMo'] = csqcobj.ChMo

            initial['ChTi'] = csqcobj.ChTi
            initial['ChNb'] = csqcobj.ChNb
            initial['ChZr'] = csqcobj.ChZr
            initial['ChN'] = csqcobj.ChN

            
            initial['SurfLevel'] = csqcobj.SurfLevel
            initial['SQConR'] = csqcobj.SQConR
            
            initial['PipeEdgeNote'] = csqcobj.PipeEdgeNote
            initial['PipeEdgeNoteT'] = csqcobj.PipeEdgeNote

            initial['Flaring'] = csqcobj.Flaring
            initial['Flattening'] = csqcobj.Flattening

            initial['Flattening90'] = csqcobj.Flattening90
            initial['InBead'] = csqcobj.InBead
            initial['SQConR'] = csqcobj.SQConR

            initial['Straight'] = csqcobj.Straight
            initial['Others'] = csqcobj.Notes
            initial['SQWSPost'] = csqcobj.SQWSPost
            
            
        
        
            salevelobj = surflevel.objects.get(SurfLevel = csqcobj.SurfLevel)

            initial['SurfCondE'] = salevelobj.ENotes
            initial['SurfCondV'] = salevelobj.VNotes
        except csqc.DoesNotExist:
                initial['AdjOD'] = None
                initial['AdjOD'] = None
                initial['AdjOD'] = None
                initial['AdjID'] = None
                initial['AdjWT'] = None
                initial['AdjL'] = None
                initial['TS'] = None
                initial['YP'] = None
                initial['EL'] = None
                initial['Hardness'] = None
                initial['ChC'] = None
                initial['ChSi'] = None
                initial['ChMn'] = None
                initial['ChP'] = None
                initial['ChS'] = None
                initial['ChAL'] = None
                initial['ChNi'] = None
                initial['ChCr'] = None
                initial['CHMo'] = None
                initial['ChTi'] = None
                initial['ChNb'] = None
                initial['ChZr'] = None
                initial['ChN'] = None
                initial['SurfLevel'] = None
                initial['SQConR'] = None
                initial['PipeEdgeNote'] = None
                initial['PipeEdgeNoteT'] = None
                initial['Flaring'] = None
                initial['Flattening'] = None
                initial['Flattening90'] = None
                initial['InBead'] = None
                initial['SQConR'] = None
                initial['Straight'] = None
                initial['Others'] = None
                initial['SQWSPost'] = None
                initial['SurfCondE'] = None
                initial['SurfCondV'] = None
		
            
		

		    # Coatching =  IIF(CS.PipeGrade = 'SUS409L','Not Apply','Outside & Inside: Light oil/ trong và ngoài ống phủ 1 lớp mỏng dầu'),
            # initial['PipeStd'] = csobj.PipeStd

            # initial['HeatTreat'] = csobj.HeatTreat
            # initial['SKind'] = csobj.SKind
            # initial['PKind'] = csobj.PKind
            



            


        return initial
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
        messages.success(self.request, 'SA created successfully at ' + timezone.now().strftime("%Y-%m-%d %H:%M:%S"))
        # Call the parent class's form_valid() method to save the instance
        response = super().form_valid(form)

        # Perform any additional processing here

        return response

class SAUpdateView(LoginRequiredMixin, UpdateView):
    model = sa
    
    form_class = SAUpdateForm


    # pass user_name to the form
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        group_names = self.request.user.groups.values_list('name', flat=True)
        kwargs['group_names'] = group_names
        return kwargs
    
    def get_success_url(self):
        
        # data = self.form.cleaned_data
        # return reverse_lazy('cs-update', kwargs={'pk': self.object.pk})
        sne_cs = self.request.POST.get('save-edit-sa')
        snp_cs = self.request.POST.get('save-print-sa')
        # sne_sa = self.request.POST.get('save-edit-sa')
        # snverup_cs = self.request.POST.get('save-upver-cs') # Save n version up - Upgrade version
        # sna_sa = self.request.POST.get('save-add-sa')   # Save n add new sa


        
        
        
        if sne_cs:
        #    return reverse('cs-update', args=(self.kwargs['pk'],))
           return reverse_lazy('sa-update', kwargs={'pk': self.object.pk})
        
        if snp_cs:
           return reverse_lazy('sa-detail', kwargs={'pk': self.object.pk})
        
        # if sne_sa:
        #    if sa.objects.filter(SANo=self.object.SANo):
        #        return reverse_lazy('sa-update', kwargs={'pk': self.object.SANo}) 
        #    else:
        #        return reverse_lazy('sa-add', kwargs={'pk': self.object.SANo, 'cs': self.object.CSNo})     
        # # if sna_sa:
        # #    return reverse_lazy('sa-add', kwargs={'pk': self.object.SANo, 'cs': self.object.CSNo}) 
        
        # if snverup_cs:
        # #    return reverse('cs-add')
        #    return reverse_lazy('cs-add', kwargs={'pk':int(self.object.pk) + 1})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['AppHistory'] = sa.objects.filter(SANo__startswith=self.object.pk[:7]).order_by('-SANo')
        context['RelatedCS'] = cs.objects.filter(SANo__startswith=self.object.pk[:7])
        return context

    def form_valid(self, form):
        self.form = form
 
        context = self.get_context_data()

        messages.success(self.request, 'SPEC Agreement updated successfully at ' + timezone.localtime(timezone.now()).strftime("%Y-%m-%d %H:%M:%S"))
        # Retrieve the existing record
        my_model = self.get_object()

        # Get the field value before the update
        current_value_SAApp = my_model.SAApp
        self.object.LastUser = self.request.user.username
        self.object.LastimeUser = timezone.now()  
        # Update the record
        response = super().form_valid(form)

        if (current_value_SAApp != self.object.SAApp) :
           
            url = reverse('sa-update', kwargs={'pk': form.cleaned_data['SANo']})
            self.object.AppDate = timezone.now()
            subject = 'SPEC Agreement has been approved ' +  timezone.localtime(timezone.now()).strftime("%Y-%m-%d %H:%M:%S")
            message = 'SPEC Agreement No: ' + form.cleaned_data['SANo'] + ' is approved at: ' + self.request.build_absolute_uri(url)
            sender = 'support@vnsp.vn'
            # recipients = EmailReport.objects.values_list('ReciEmail', flat=True)
            recipients = EmailReport.objects.filter(ActionName='SAAppNote').values_list('ReciEmail', flat=True)

            send_mail(subject, message, sender, recipients)


        # Tracking editor
          
        return response

class SADetailView(DetailView):
    model = sa

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['cs_related_list'] = cs.objects.filter(SANo=self.object.SANo)
        context['AppHistory'] = sa.objects.filter(SANo__startswith=self.object.pk[:7]).order_by('-SANo')
        return context
    
        
        
class SADeleteView(LoginRequiredMixin, DeleteView):
    model = sa
    success_url = reverse_lazy('SAHome')