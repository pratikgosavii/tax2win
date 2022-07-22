

from django import forms

from .models import *
from django.contrib.admin.widgets import  AdminDateWidget, AdminTimeWidget, AdminSplitDateTime



class enquire_Form(forms.ModelForm):
    class Meta:
        model = enquire
        fields = '__all__'
      
       

class prices_enquire_Form(forms.ModelForm):
    class Meta:
        model = prices_enquire
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
        widgets = {

            'date_time' : forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': "form-control"}),
        }
      
       

class indirect_taxcation_Form(forms.ModelForm):
    class Meta:
        model = indirect_taxcation
        fields = '__all__'
        widgets = {

            'date_time' : forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': "form-control"}),
        }
       

class virtual_book_Form(forms.ModelForm):
    class Meta:
        model = virtual_book_questions
        fields = '__all__'
        widgets = {

            'date_time' : forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': "form-control"}),
        }

class company_llp_Form(forms.ModelForm):
    class Meta:
        model = company_llp_questions
        fields = '__all__'
        widgets = {

            'date_time' : forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': "form-control"}),
        }
       
       

class unlock_eca_Form(forms.ModelForm):
    class Meta:
        model = file_yourself
        fields = '__all__'
        widgets = {

            'date_time' : forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': "form-control"}),
        }
       
       

class file_yourself_Form(forms.ModelForm):
    class Meta:
        model = file_yourself
        fields = '__all__'
      
        widgets = {

            'date_time' : forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': "form-control"}),
        }