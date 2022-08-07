from pyexpat import model
from random import choices
from secrets import choice
from django.db import models
from django.forms import CharField

from django.contrib.auth import get_user_model

User=get_user_model()

# Create your models here.

class enquire(models.Model):

    name = models.CharField(max_length=50)
    date_time = models.DateTimeField(auto_now=False)
    mobile = models.IntegerField()

    salary_income = models.BooleanField()
    presumptive_income = models.BooleanField()
    house_property_income = models.BooleanField()
    other_sources_income = models.BooleanField()
    capital_gain_income = models.BooleanField()
    foreign_income = models.BooleanField()

    


    def __str__(self):
        return self.name



class refund_status(models.Model):

    name = models.CharField(max_length=50)
    date_time = models.DateTimeField(auto_now=False)
    mobile = models.IntegerField()
    

    def __str__(self):
        return self.name



status_CHOICES =(
    ("Done", "Done"),
    ("Pending", "Pending"),
    ("Cancle", "Cancle"),
    ("Reschedule", "Reschedule"),
)
  

plan_CHOICES =(
    ("Standard", "Standard"),
    ("MultipleF-16", "MultipleF-16"),
    ("Business Income", "Business Income"),
    ("Capital Gain", "Capital Gain"),
)
  

class prices_enquire(models.Model):

    name = models.CharField(max_length=50)
    date_time = models.DateTimeField(auto_now=False)
    mobile = models.IntegerField()
    user = models.ForeignKey(User , on_delete=models.CASCADE, blank=True, null=True)
    comment = models.CharField(max_length=500, blank=True, null=True)
    plan = models.CharField(choices = plan_CHOICES, max_length=50, blank=True, null=True)


class direct_taxcation(models.Model):

    name = models.CharField(max_length=50)
    date_time = models.DateTimeField(auto_now=False)
    mobile = models.IntegerField()
    user = models.ForeignKey(User , on_delete=models.CASCADE, blank=True, null=True)
    comment = models.CharField(max_length=500, blank=True, null=True)
    status = models.CharField(choices = status_CHOICES, max_length=50, blank=True, null=True)


    Registration_on_portal = models.BooleanField()
    Income_Tax_Return_Filings = models.BooleanField()
    Income_Tax_Audit_filings = models.BooleanField()
    Assesment_filings = models.BooleanField()
    Tax_planning = models.BooleanField()
    Advice_Consultancy = models.BooleanField()
    

    def __str__(self):
        return self.name


class indirect_taxcation(models.Model):

    name = models.CharField(max_length=50)
    date_time = models.DateTimeField(auto_now=False)
    mobile = models.IntegerField()
    user = models.ForeignKey(User , on_delete=models.CASCADE, blank=True, null=True)
    comment = models.CharField(max_length=500, blank=True, null=True)
    status = models.CharField(choices = status_CHOICES, max_length=50, blank=True, null=True)

    
    Registration_on_portal = models.BooleanField()
    Tax_planning = models.BooleanField()
    Advice_Consultancy = models.BooleanField()

    def __str__(self):
        return self.name




class company_llp_questions(models.Model):

    name = models.CharField(max_length=50)
    date_time = models.DateTimeField(auto_now=False)
    mobile = models.IntegerField()
    user = models.ForeignKey(User , on_delete=models.CASCADE, blank=True, null=True)
    comment = models.CharField(max_length=500, blank=True, null=True)
    status = models.CharField(choices = status_CHOICES, max_length=50, blank=True, null=True)


    Name_approval_application = models.BooleanField()
    Company_LLP_registration = models.BooleanField()
    All_other_MCA_compliances = models.BooleanField()

    
    def __str__(self):
        return self.name




class virtual_book_questions(models.Model):

    name = models.CharField(max_length=50)
    date_time = models.DateTimeField(auto_now=False)
    mobile = models.IntegerField()
    user = models.ForeignKey(User , on_delete=models.CASCADE, blank=True, null=True)
    comment = models.CharField(max_length=500, blank=True, null=True)
    status = models.CharField(choices = status_CHOICES, max_length=50, blank=True, null=True)

    
    Book_keeping_and_accountancy = models.BooleanField()
    Finalisation_of_accounts_books = models.BooleanField()
    MIS_reports_Receivables_Ageing_report  = models.BooleanField()


class contact(models.Model):

    name = models.CharField(max_length=50)
    mobile_no = models.IntegerField()
    email = models.CharField(max_length=50)
    comments = models.CharField(max_length=500)
    date_time = models.DateTimeField(auto_now=True)

    

    

class file_yourself(models.Model):

    name = models.CharField(max_length=50)
    mobile_no = models.IntegerField()
    date_time = models.DateTimeField(auto_now=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    

class add_itrdate(models.Model):

    date_time = models.DateTimeField(auto_now=False)


    





from django.contrib import admin
from .models import *

# Register your models here.




admin.site.register(enquire)
admin.site.register(direct_taxcation)
admin.site.register(indirect_taxcation)
admin.site.register(virtual_book_questions)
admin.site.register(company_llp_questions)