from django.urls import path
from .views import *

urlpatterns = [

    path('emailreport/list/', EmailRListView.as_view(), name='emailreport-list'),
    path('emailreport/create/', EmailRCreateView.as_view(), name='emailreport-create'),
    path('emailreport/<str:pk>/', EmailRUpdateView.as_view(), name='emailreport-update'),

    path('surflevel/list/', SLListView.as_view(), name='surflevel-list'),
    path('surflevel/create/', SLCreateView.as_view(), name='surflevel-create'),
    path('surflevel/<str:pk>/', SLUpdateView.as_view(), name='surflevel-update'),
    path('surflevel/<str:pk>/detail', SLDetailView.as_view(), name='surflevel-detail'),
    path('surflevel/<str:pk>/delete/', SLDeleteView.as_view(), name='surflevel-delete'),

    path('cust/list/', CustlListView.as_view(), name='cust-list'),
    path('cust/create/', CustCreateView.as_view(), name='cust-create'),
    path('cust/<str:pk>/', CustUpdateView.as_view(), name='cust-update'),
    path('cust/<str:pk>/detail', CustDetailView.as_view(), name='cust-detail'),
    path('cust/<str:pk>/delete/', CustDeleteView.as_view(), name='cust-delete'),

    path('pgrade/list/', PGradeListView.as_view(), name='pgrade-list'),
    path('pgrade/create/', PGradeCreateView.as_view(), name='pgrade-create'),
    path('pgrade/<str:pk>/', PGradeUpdateView.as_view(), name='pgrade-update'),
    path('pgrade/<str:pk>/detail', PGradeDetailView.as_view(), name='pgrade-detail'),
    path('pgrade/<str:pk>/delete/', PGradeDeleteView.as_view(), name='pgrade-delete'),

    path('cgrade/list/', CGradeListView.as_view(), name='cgrade-list'),
    path('cgrade/create/', CGradeCreateView.as_view(), name='cgrade-create'),
    path('cgrade/<str:pk>/', CGradeUpdateView.as_view(), name='cgrade-update'),
    path('cgrade/<str:pk>/detail', CGradeDetailView.as_view(), name='cgrade-detail'),
    path('cgrade/<str:pk>/delete/', CGradeDeleteView.as_view(), name='cgrade-delete'),
]