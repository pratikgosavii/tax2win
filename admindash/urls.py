"""tax2win URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from .views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   
    path('index', index, name="admin-index"),
    path('admin-direct-tax', admin_direct_tax, name="admin_direct_tax"),
    path('admin-indirect-tax', admin_indirect_tax, name="admin_indirect_tax"),
    path('admin-comapny', admin_company, name="admin_company"),
    path('admin-virtual', admin_virtual, name="admin_virtual"),
    path('admin-prices-enquire', admin_prices_enquire, name="admin_prices_enquire"),
    path('admin-contact-us', admin_contact_us, name="admin_contact_us"),
  
    path('admin-selffiling-ca-assisted', selfiling_eca, name="selfiling_eca"),
  


    path('update-direct-tax/<request_id>', update_direct_tax, name="update_direct_tax"),
    path('update-indirect-tax/<request_id>', update_indirect_tax, name="update_indirect_tax"),
    path('update-company-tax/<request_id>', update_comapny_tax, name="update_comapny_tax"),
    path('update-virtual-tax/<request_id>', update_virtual_tax, name="update_virtual_tax"),

    path('delete-direct-tax/<request_id>', delete_direct_tax, name="delete_direct_tax"),
    path('delete-indirect-tax/<request_id>', delete_indirect_tax, name="delete_indirect_tax"),
    path('delete-company-tax/<request_id>', delete_comapny_tax, name="delete_comapny_tax"),
    path('delete-virtual-tax/<request_id>', delete_virtual_tax, name="delete_virtual_tax"),



] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)