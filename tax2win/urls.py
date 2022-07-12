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
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('', index, name="index"),
    path('direct-taxcation-questions', direct_taxcation_questions, name="direct_taxcation_questions"),
    path('indirect-taxcation-questions', indirect_taxcation_questions, name="indirect_taxcation_questions"),
    path('virtual-book-keeping-questions', virtual_book_questions, name="virtual_book_questions"),
    path('company-llp-questions', company_llp_questions, name="company_llp_questions"),
    path('submit-request', submit, name="submit_request"),
    path('refund-status', refund_status, name="refund_status"),
    path('submit-services-request', submit_services_request, name="submit_services_request"),

    path('pricing', pricing, name="pricing"),
    path('privacy-policy', privacy_policy, name="privacy_policy"),
    path('terms-condtion', terms_condition, name="terms_condition"),
    
    path('admin-view-categories', admin_view, name="admin_view"),

]

urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)