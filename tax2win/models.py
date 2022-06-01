from pyexpat import model
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



from django.contrib import admin
from .models import *

# Register your models here.




admin.site.register(enquire)