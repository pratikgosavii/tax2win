

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
      


class contact_Form(forms.ModelForm):
    class Meta:
        model = contact
        fields = '__all__'
      
       


class direct_taxcation_Form(forms.ModelForm):
    class Meta:
        model = direct_taxcation
        fields = '__all__'
      
       

class indirect_taxcation_Form(forms.ModelForm):
    class Meta:
        model = indirect_taxcation
        fields = '__all__'
      
       

class virtual_book_questions_Form(forms.ModelForm):
    class Meta:
        model = virtual_book_questions
        fields = '__all__'
      
       

class company_llp_questions_Form(forms.ModelForm):
    class Meta:
        model = company_llp_questions
        fields = '__all__'
      
       
       

class unlock_eca_Form(forms.ModelForm):
    class Meta:
        model = Unlock_eca
        fields = '__all__'
      
       
       

class file_yourself_Form(forms.ModelForm):
    class Meta:
        model = file_yourself
        fields = '__all__'
      
       