from django.shortcuts import render

# Create your views here.
from django.views.generic.edit import UpdateView, CreateView
from django.views.generic import DetailView, ListView, DeleteView
from django.urls import reverse_lazy
from .models import cust, pipegrade, coilgrade, surflevel, EmailReport
from django.contrib import messages

# Email report
class EmailRCreateView(CreateView):
    model = EmailReport
    fields = '__all__'
    success_url = reverse_lazy('emailreport-list')

class EmailRListView(ListView):
    model = EmailReport
    context_object_name = 'emailreport_list'

class EmailRUpdateView(UpdateView):
    model = EmailReport
    fields = '__all__'
    # template_name_suffix = '_update_form'
    success_url = reverse_lazy('emailreport-list')

# Surface level setting
class SLCreateView(CreateView):
    model = surflevel
    fields = '__all__'
    success_url = reverse_lazy('surflevel-list')

class SLUpdateView(UpdateView):
    model = surflevel
    fields = '__all__'
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('surflevel-list')

class SLDetailView(DetailView):
    model = surflevel

class SLDeleteView(DeleteView):
    model = surflevel
    success_url = reverse_lazy('surflevel-list')

class SLListView(ListView):
    model = surflevel
    context_object_name = 'SL_list'

# Customer setting
class CustCreateView(CreateView):
    model = cust
    fields = '__all__'
    success_url = reverse_lazy('cust-list')

class CustUpdateView(UpdateView):
    model = cust
    fields = '__all__'
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('cust-list')

class CustDetailView(DetailView):
    model = cust

class CustDeleteView(DeleteView):
    model = cust
    success_url = reverse_lazy('cust-list')

class CustlListView(ListView):
    model = cust
    context_object_name = 'cust_list'


# Pipe Grade setting
class PGradeCreateView(CreateView):
    model = pipegrade
    fields = '__all__'
    success_url = reverse_lazy('pgrade-list')

class PGradeUpdateView(UpdateView):
    model = pipegrade
    fields = '__all__'
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('pgrade-list')

class PGradeDetailView(DetailView):
    model = pipegrade

class PGradeDeleteView(DeleteView):
    model = pipegrade
    success_url = reverse_lazy('pgrade-list')

class PGradeListView(ListView):
    model = pipegrade


# Coil Grade setting
class CGradeCreateView(CreateView):
    model = coilgrade
    fields = '__all__'
    success_url = reverse_lazy('cgrade-list')

class CGradeUpdateView(UpdateView):
    model = coilgrade
    fields = '__all__'
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('cgrade-list')

class CGradeDetailView(DetailView):
    model = coilgrade

class CGradeDeleteView(DeleteView):
    model = coilgrade
    success_url = reverse_lazy('cgrade-list')

class CGradeListView(ListView):
    model = coilgrade
    