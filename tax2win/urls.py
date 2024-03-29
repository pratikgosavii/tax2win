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
    path('admin-dashboard/', include('admindash.urls')),
    path('', index, name="index"),
    path('direct-taxcation-questions', direct_taxcation_questions, name="direct_taxcation_questions"),
    path('indirect-taxcation-questions', indirect_taxcation_questions, name="indirect_taxcation_questions"),
    path('virtual-book-keeping-questions', virtual_book_questions, name="virtual_book_questions"),
    path('company-llp-questions', company_llp_questions, name="company_llp_questions"),
    path('submit-request', submit, name="submit_request"),
    path('refund-status', refund_status, name="refund_status"),
    path('submit-services-request', submit_services_request, name="submit_services_request"),

    path('prices-enquire', prices_enquire_view, name="prices_enquire"),

    path('unlock-eca', unlock_eca, name="unlock_eca_url"),
    path('file-yourself', file_yourself_view, name="file_yourself_url"),

    path('pricing', pricing, name="pricing"),
    path('privacy-policy', privacy_policy, name="privacy_policy"),
    path('contact', contact_view, name="contact"),
    path('terms-condtion', terms_condition, name="terms_condition"),
    
    path('admin-view-categories', admin_view, name="admin_view"),
    
    path('knowledge-is-power/Income-From-Salary', Income_From_Salary,name="Income_From_Salary"),
    path('knowledge-is-power/Income-From-House-Propety', Income_From_House_Propety,name="Income_From_House_Propety"),
    path('knowledge-is-power/Income-From-Propery-Gain', Income_From_Propery_Gain,name="Income_From_Propery_Gain"),

    path('knowledge-is-power/Income-From-Business-Profession', Income_From_Busines_Profession,name="Income_From_Busines_Profession"),
    path('knowledge-is-power/Income-From-Other-Source', Income_From_Other_Source,name="Income_From_Other_Source"),
    path('knowledge-is-power/Avoid-Tax-Notices', Avoid_Tax_Notices,name="Avoid_Tax_Notices"),

    path('knowledge-is-power/Tax-Deductions-At-Sources-TDS', Tax_Deductions_At_Sources_TDS,name="TTax_Deductions_At_Sources_TDS"),
    path('knowledge-is-power/Tax-Collection-At-Sources-TCS', Tax_Collection_At_Sources_TCS,name="Tax_Collection_At_Sources_TCS"),
    path('knowledge-is-power/Due-Dates', Due_Dates,name="Due_Dates"),




] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)