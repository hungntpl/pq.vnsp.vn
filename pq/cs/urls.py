# cs urls
from django.urls import path
from .views import  *
# from .views import  CSFilter

# from .views import CSDetailView, CSFilterView
# from .views import my_model_detail

urlpatterns = [


    path('', CPFilter.as_view(), name='CSHome'),
    # path('', CSHome.as_view(), name='CSHome'),


    # path('adcheck/', adblockcheck, name='ad-block-checker'),
    # path('plist/', ParentList.as_view(), name='parents-list'),
    # path('pcreate/', ParentCreate.as_view(), name='parents-create'),
    
    # path('<str:pk>/edit2/', CSEditView, name='cs-edit'),
    path('exp/', export_data, name="export-data"),
    path('imp/', import_data, name="cs-import-data"),
    path('add/<int:pk>/', CSCreateView.as_view(), name='cs-add'),
    path('add/', CSCreateView.as_view(), name='cs-add'),
    
    # path('elist/', CSListEditView, name='cs-edit-list'),

    # path('create/', CSCreate.as_view(), name='create_product'),
    
    
    # path('delete-image/<int:pk>/', delete_image, name='delete_image'),
    # path('delete-variant/<int:pk>/', delete_variant, name='delete_variant'),
    # path('<str:pk>/edit/', MyUpdateView.as_view(), name='cs-update'),
    # path('<int:pk>/my_model/', my_model_detail, name='my_model_detail'),
    
    # path('<str:pk>/pdf/', CSDetailView.as_view(), name="cs-pdf"),
    # path('<str:pk>/detail/', GeneratePdf.as_view(), name='cs-pdf'),
    path('<str:pk>/', CSUpdateView.as_view(), name='cs-update'),
    path('<str:pk>/detail/', CSDetailView.as_view(), name='cs-detail'), # prompt to print preview
    path('<str:pk>/delete/', CSDeleteView.as_view(), name='cs-delete'),
    path('<str:pk>/pdf/', cs_pdf, name="cs-pdf"),



    # path('<str:pk>/approved/', CSApprovedUpdateView.as_view(), name='csapp-update'),
    # path('<str:pk>/approvedlist/', CSApprovedListView.as_view(), name='csapp-list'),
    # path('<str:pk>/approveddetail/', CSApprovedDetailView.as_view(), name='csapp-detail'),
    
    

    
    
    # path('usersearch', search, name='USearch'),
    # path('', CSListView.as_view(), name='CSHome'),
    
] 

