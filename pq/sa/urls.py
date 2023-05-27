# sa urls home 
from django.urls import path
from .views import SAHome
from .views import SADetailView, SACreateView, SAUpdateView, SADeleteView

urlpatterns = [

    path('', SAHome.as_view(), name='SAHome'),
    # path('', SAFilterView.as_view(), name='SAHome'),
    # path('', SAListView.as_view(), name='SAHome'),
    # path('add/<int:pk>/', SACreateView.as_view(), name='sa-add'),
    
    path('add/', SACreateView.as_view(), name='sa-add'),
    path('add/<str:pk>of<str:cs>/', SACreateView.as_view(), name='sa-add'),
    path('<str:pk>/delete/', SADeleteView.as_view(), name='sa-delete'),
    path('<str:pk>/', SAUpdateView.as_view(), name='sa-update'),
    path('<str:pk>/detail/', SADetailView.as_view(), name='sa-detail'),
    
]