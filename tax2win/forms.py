

from django import forms

from .models import *
from django.contrib.admin.widgets import  AdminDateWidget, AdminTimeWidget, AdminSplitDateTime



class enquire_Form(forms.ModelForm):
    class Meta:
        model = enquire
        fields = '__all__'
      
       