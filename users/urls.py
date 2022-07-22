from django.urls import path

from .views import *

from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('login/', login_page, name='login'),
    path('register/', register_page, name='register'),
    path('logout/', logout_page, name='logout'),
    path('your-requests/', your_requests, name='your_requests'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
