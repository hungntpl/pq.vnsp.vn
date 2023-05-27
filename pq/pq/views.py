from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import NameForm
from django.shortcuts import render
from django.views.generic.edit import FormView
from django.forms import ModelForm
from .forms import CSModelForm
import json
import datetime
from django.views.generic import ListView
from cs.models import cs
from sa.models import sa
from itertools import chain
from django.db import connection
from datetime import datetime, timedelta
from .forms import ReloadDatabase
from django.db import connection
from django.contrib import messages
from django.utils import timezone
# from operator import attrgetter


def reload_database(request):
    if request.method == 'POST':
        form = ReloadDatabase(request.POST)
        if form.is_valid():
            # Process the form data here
            confirm = form.cleaned_data['confirm']
            # confirm = "reloaded at"
            cursor = connection.cursor()
            if confirm == "OK":
                try:
                    cursor.execute('EXEC [dbo].[get_pipegrade]')
                    cursor.execute('EXEC [dbo].[get_coilgrade]')
                    
                    cursor.execute('EXEC [dbo].[get_cust]')
                    cursor.execute('EXEC [dbo].[get_sa]')
                    cursor.execute('EXEC [dbo].[get_cs]')

                    cursor.execute('EXEC [dbo].[get_coilprocess]')
                    cursor.execute('EXEC [dbo].[get_csqc]')
                    cursor.execute('EXEC [dbo].[get_cspi]')
                    # result_set = cursor.fetchall()
                    messages.success(request, 'Database is reloaded successfully at ' + timezone.now().strftime("%Y-%m-%d %H:%M:%S"))
                finally:
                    cursor.close()
                
            # Perform necessary actions with the data
    else:
        form = ReloadDatabase()
    return render(request, 'pq/reload_database.html', {'form': form})

class SACSSearch(LoginRequiredMixin, ListView):
    model = sa
    
    template_name = 'pq/sacs_search.html'
    context_object_name = 'sa_list'
    ordering = ['-LastimeUser']

    def get_queryset(self):
        # cursor = connection.cursor()
        # try:
        #     cursor.execute('EXEC [dbo].[get_cust]')
        #     cursor.execute('EXEC [dbo].[get_pipegrade]')
        #     cursor.execute('EXEC [dbo].[get_coilgrade]')
        #     # cursor.execute('EXEC [dbo].[get_sa]') đang bị lỗi vì đổi CustID, PipeGrade từ field thường sang foreign key 
        #     cursor.execute('EXEC [dbo].[get_cs]')
            
        # finally:
        #     cursor.close()
        # if self.request.method == 'POST':
        #     # Get parameter from POST data
        #     query = self.request.POST.get('q')
        #     # Filter queryset based on parameter
        #     queryset = queryset.filter(SANo__icontains=query)
        #     # queryset = queryset.order_by('-LastimeUser')[:25]
        #     # queryset = MyModel.objects.filter(my_field=my_param)
        # else:
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(SANo__icontains=query)
        queryset = queryset.order_by('-LastimeUser')[:25]
        return queryset
    
    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     query = self.request.POST.get('q')
    #     if query:
    #         queryset = queryset.filter(SANo__icontains=query)
    #     queryset = queryset.order_by('-LastimeUser')[:25]
    #     return queryset

    def get_context_data(self, **kwargs):
        

        context = super().get_context_data(**kwargs)
        # context['cs_list'] = cs.objects.all()
        context['cs_list'] = cs.objects.all().order_by('-LastimeUser')[:25]

        query = self.request.GET.get('q')
        if query:
            context['cs_list'] = cs.objects.all().filter(CSNo__icontains=query)
        

       
        return context


class SACS(LoginRequiredMixin, ListView):
    model = sa
    # paginate_by = 20
    template_name = 'pq/sacslist.html'
    context_object_name = 'sa_list'
    ordering = ['-LastimeUser']

    def get_queryset(self):
        top20 = sa.objects.all().order_by('-LastimeUser')[:25]
        return top20
    
    def get_context_data(self, **kwargs):
        cursor = connection.cursor()
        try:
            
            cursor.execute('EXEC [dbo].[get_sa]')
            cursor.execute('EXEC [dbo].[get_cs]')
            # result_set = cursor.fetchall()
        finally:
            cursor.close()

        context = super().get_context_data(**kwargs)
        # context['picture'] = Picture.objects.filter(your_condition)
        context['cs_list'] = cs.objects.all().order_by('-LastimeUser')[:25]
        # context['related_objects'] = cs.objects.related_set.all()
        # context['cs_related_list'] = cs.objects.filter(SANo=sa.SANo)
        # context['cs_related_list'] = cs.objects.all().order_by('-LastimeUser')[:10]
        return context

# def SearchSA(request):
#     if request.method == "POST":
#         form = inputmanual(request.POST)
#             if form.is_valid():
#                 pk = form.cleaned_data['pk']
#             return redirect('submit export note', pk=pk)
class CombinedModel:
    def __init__(self, cs, sa):
        self.cs = cs
        self.sa = sa

class CSSAListView(LoginRequiredMixin, ListView):
    # model = cs
    # login_url = 'login'
    # login_required = True
    paginate_by = 100
    template_name = 'pq/cssalist.html'
    context_object_name = 'cssa'
    # ordering = ['-cs.LastimeUser']
    def get_queryset(self):
        # update latest data
        cursor = connection.cursor()
        try:
            
            cursor.execute('EXEC [dbo].[get_sa]')
            cursor.execute('EXEC [dbo].[get_cs]')
            # result_set = cursor.fetchall()
        finally:
            cursor.close()
        

        model1_list = cs.objects.all()
        model2_list = sa.objects.all()
        combined_list = [CombinedModel(cs, sa) for cs, sa in zip(model1_list, model2_list)]

        # get the last 90 modified items
        today = datetime.today()
        three_months_ago = today - timedelta(days=90)

        combined_list = sorted(combined_list, key=lambda x: (x.sa.LastimeUser is None, x.sa.LastimeUser), reverse=True)

       
        return combined_list


    # def get_queryset(self):
    #     cursor = connection.cursor()
    #     try:
    #         cursor.execute('EXEC [dbo].[get_cs]')
    #         # result_set = cursor.fetchall()
    #     finally:
    #         cursor.close()
            
    #     today = datetime.today()
    #     three_months_ago = today - timedelta(days=90)

    #     queryset = list(chain(cs.objects.all(), sa.objects.all()))
        
    #     return queryset
  
    # def get_queryset(self):
    #     cursor = connection.cursor()
    #     try:
    #         cursor.execute('EXEC [dbo].[get_cs]')
    #         # result_set = cursor.fetchall()
    #     finally:
    #         cursor.close()
            
    #     today = datetime.today()
    #     three_months_ago = today - timedelta(days=90)
    #     queryset = super().get_queryset()
    #     # queryset = queryset.annotate(count=Count('CSNo'))
    #     return queryset.filter(LastimeUser__gte=three_months_ago)

class PQHome(LoginRequiredMixin, FormView):

    form_class = NameForm
    template_name = "pq/home.html"
    success_url ="/" 

    def form_valid(self, form):
        

        self.request.session['chart_type'] = form.cleaned_data.get('chart_type')
        self.request.session['pro_date'] = json.dumps(form.cleaned_data.get('pro_date'), default=str )


       
        return super(PQHome, self).form_valid(form)
    
    def get_form_kwargs(self):
        """
        The FormMixin uses this to populate the data from the POST request.
        Here, first try to populate it from the session data, if any;
        if there is POST data, it should override the session data.
        """
        # kwargs = {'data': self.request.session.get('form_class_data', None)}
        kwargs = super(PQHome, self).get_form_kwargs()
        # kwargs.update(super(HomePageView, self).get_form_kwargs())
        return kwargs

    def get_context_data(self, **kargs):
        context = super(PQHome, self).get_context_data(**kargs)
        if 'chart_type' in self.request.session:
            context["surl"] = self.request.session['chart_type']

        else:
            context["surl"] = "line"
            context["pro_date"]= datetime.date.today()
        return context
    
    def get_initial(self):
        # call super if needed
        if 'chart_type' in self.request.session:
            return {'chart_type': self.request.session['chart_type'], 'pro_date': json.loads(self.request.session['pro_date'])}
        else:
            return {'chart_type': 'line','pro_date': datetime.date.today()}

def PQHomeCSSA(request):
    if request.method == 'POST':
        form = CSModelForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CSModelForm()

    return render(request, 'pq/home_cssa.html', {'form': form})