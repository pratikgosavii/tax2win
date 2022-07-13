from pyexpat import model
from random import choices
from secrets import choice
from django.db import models
from django.forms import CharField

# Create your models here.

class enquire(models.Model):

    name = models.CharField(max_length=50)
    date_time = models.DateTimeField(auto_now=False, auto_now_add=False)
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
    date_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    mobile = models.IntegerField()
    

    def __str__(self):
        return self.name




services_CHOICES1 =(
    ("Registration on portal", "Registration on portal"),
    ("Income Tax Return Filings", "Income Tax Return Filings"),
    ("Income Tax Audit filings", "Income Tax Audit filings"),
    ("Assesment filings", "Assesment filings"),
    ("Tax planning", "Tax planning"),
    ("Advice_Consultancy", "Advice/Consultancy"),
   
)


services_CHOICES2 =(
    ("Registration on portal", "Registration on portal"),
    ("Tax planning", "Tax planning"),
    ("Advice_Consultancy", "Advice/Consultancy"),
    
)

services_CHOICES3 =(
    ("Name approval application", " Name approval application"),
    ("Company_LLP registration", "Company/LLP registration"),
    ("All other MCA compliances", "All other MCA compliances"),
    
)

services_CHOICES4 =(
    ("Book keeping and accountancy", "Book keeping and accountancy"),
    ("Finalisation of accounts books", "Finalisation of accounts books"),
    ("MIS reports-Receivables Ageing report", "MIS reports-Receivables Ageing report"),
    
)




class direct_taxcation(models.Model):

    name = models.CharField(max_length=50)
    date_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    mobile = models.IntegerField()

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
    date_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    mobile = models.IntegerField()
    
    Registration_on_portal = models.BooleanField()
    Tax_planning = models.BooleanField()
    Advice_Consultancy = models.BooleanField()

    def __str__(self):
        return self.name




class company_llp_questions(models.Model):

    name = models.CharField(max_length=50)
    date_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    mobile = models.IntegerField()

    Name_approval_application = models.BooleanField()
    Company_LLP_registration = models.BooleanField()
    All_other_MCA_compliances = models.BooleanField()

    
    def __str__(self):
        return self.name




class virtual_book_questions(models.Model):

    name = models.CharField(max_length=50)
    date_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    mobile = models.IntegerField()
    
    Book_keeping_and_accountancy = models.BooleanField()
    Finalisation_of_accounts_books = models.BooleanField()
    MIS_reports_Receivables_Ageing_report  = models.BooleanField()


class contact(models.Model):

    name = models.CharField(max_length=50)
    mobile_no = models.IntegerField()
    email = models.CharField(max_length=50)
    comments = models.CharField(max_length=500)
    date_time = models.DateTimeField(auto_now=True)

    

class Unlock_eca(models.Model):

    name = models.CharField(max_length=50)
    mobile_no = models.IntegerField()
    date_time = models.DateTimeField(auto_now=True)


    
    

class file_yourself(models.Model):

    name = models.CharField(max_length=50)
    mobile_no = models.IntegerField()
    date_time = models.DateTimeField(auto_now=True)


    





from django.contrib import admin
from .models import *

# Register your models here.




admin.site.register(enquire)
admin.site.register(direct_taxcation)
admin.site.register(indirect_taxcation)
admin.site.register(virtual_book_questions)
admin.site.register(company_llp_questions)