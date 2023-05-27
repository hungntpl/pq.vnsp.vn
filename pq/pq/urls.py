"""pq URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from .views import CSSAListView, SACS, SACSSearch, reload_database
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', SACSSearch.as_view(), name='home'),
    # path('cust/list/', SACSSearch.as_view(), name='sacs-search'),
    # path('cssahome', CSSAListView.as_view(), name='CSSAHomeList'),
    # path('cssa', views.PQHomeCSSA, name='PQHomeCSSA'),
    # path('home', views.PQHome.as_view(), name='PQHome'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls'), name='login'),
    path('accounts/logout/', include('django.contrib.auth.urls'), name='logout'),
    path('accounts/password_change/', include('django.contrib.auth.urls'), name='password_change'),

    path('accounts/password_change/done/', include('django.contrib.auth.urls'), name='password_change_done'),
    path('accounts/password_reset/done/', include('django.contrib.auth.urls'), name='password_reset_done'),
    path('accounts/password_reset/', include('django.contrib.auth.urls'), name='password_reset'),
    
    # path('accounts/reset/<uidb64>/<token>/', include('django.contrib.auth.urls'), name='password_reset_confirm'),
    # path('accounts/reset/done/', include('django.contrib.auth.urls'), name='password_reset_complete'),


    path('set/', include('set.urls')),
    path('cs/', include('cs.urls')),
    path('sa/', include('sa.urls')),
    path('reloaddatabase/', views.reload_database, name='reload-database'),
    # path('sa/', include('sa.urls')),
]
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "VNSP's SACS Controller"
admin.site.site_title = "VNSP's SACS Management"
admin.site.index_title = "Welcome to VNSP's SACS"
