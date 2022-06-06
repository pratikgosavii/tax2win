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




services_CHOICES =(
    ("ECA", "ECA"),
    ("Direct Taxation Advice", "Direct Taxation Advice"),
    ("ITR Filling", "ITR Filling"),
    ("File Revised Return", "File Revised Return"),
    ("Company Formation", "Company Formation"),
    ("Registration and Formation of LLPs", "Registration and Formation of LLPs"),
    ("MCA 21 Compilances", "MCA 21 Compilances"),
    ("GST Registration", "GST Registration"),
    ("Income Tax Assessment and Appeals", "Income Tax Assessment and Appeals"),
    ("Virtual CFO Book keeping and Accountancy", "Virtual CFO Book keeping and Accountancy"),
)




class services(models.Model):

    name = models.CharField(max_length=50)
    date_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    mobile = models.IntegerField()
    services = models.CharField(choices = services_CHOICES, max_length = 50)
    

    def __str__(self):
        return self.name



from django.contrib import admin
from .models import *

# Register your models here.




admin.site.register(enquire)
admin.site.register(services)