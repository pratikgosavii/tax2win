

from django import forms

from .models import *
from django.contrib.admin.widgets import  AdminDateWidget, AdminTimeWidget, AdminSplitDateTime



class enquire_Form(forms.ModelForm):
    class Meta:
        model = enquire
        fields = '__all__'
      
       


class refund_status_Form(forms.ModelForm):
    class Meta:
        model = refund_status
        fields = '__all__'
      
       


class services_Form(forms.ModelForm):
    class Meta:
        model = services
        fields = '__all__'
      
       