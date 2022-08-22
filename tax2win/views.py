from email import message
import io
from multiprocessing import context
from statistics import variance
from django.contrib import messages
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import FileResponse, HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.core import serializers
from django.contrib.auth.decorators import login_required
from datetime import date
from django.urls import reverse
import dateutil.parser
from datetime import date
from django.http import FileResponse, Http404
from itertools import chain

from django.contrib.auth.decorators import user_passes_test


#imports for bill generate

from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch,cm,mm
from reportlab.pdfgen.canvas import Canvas
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle, Frame, Paragraph, Spacer
import pdfkit


import csv
import mimetypes

from .forms import *

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


from datetime import datetime
import pytz

IST = pytz.timezone('Asia/Kolkata')

def index(request):


    from datetime import datetime
    from dateutil.parser import parse

    # Solution
    bday = "July 24, 2022, 11:31 p.m."

    td = parse(bday)
    bday = datetime.strftime(td, '%d/%m/%Y %H:%M')

    print(bday)


    return render(request, 'index.html', {'itr_Date': bday})


@login_required(login_url='login')
def direct_taxcation_questions(request):

    if request.method == 'POST':

        date_time = request.POST.get('date_time')

        
        d = dateutil.parser.parse(date_time)
        from_date_time = d.strftime("%Y-%m-%d %H:%M:%S")

        post = request.POST.copy() 
        post.update({"date_time" : from_date_time})
        request.POST = post

        forms = direct_taxcation_Form(request.POST)

        if forms.is_valid():

            instance = forms.save(commit=False)
            instance.user = request.user
            instance.save()

            return JsonResponse({'result' : True})

        else:

            print(forms.errors)


    else:

        return render(request, 'questions/direct_taxation.html')






@login_required(login_url='login')
def indirect_taxcation_questions(request):

    
    if request.method == 'POST':

        

        date_time = request.POST.get('date_time')

        
        d = dateutil.parser.parse(date_time)
        from_date_time = d.strftime("%Y-%m-%d %H:%M:%S")

        post = request.POST.copy() 
        post.update({"date_time" : from_date_time})
        request.POST = post

        forms = indirect_taxcation_Form(request.POST)

        if forms.is_valid():

            instance = forms.save(commit=False)
            instance.user = request.user
            instance.save()

            return JsonResponse({'result' : True})

        else:

            print(forms.errors)

    else:

        return render(request, 'questions/indirect_taxation.html')





@login_required(login_url='login')
def virtual_book_questions(request):


    
    if request.method == 'POST':

        

        date_time = request.POST.get('date_time')

        
        d = dateutil.parser.parse(date_time)
        from_date_time = d.strftime("%Y-%m-%d %H:%M:%S")

        post = request.POST.copy() 
        post.update({"date_time" : from_date_time})
        request.POST = post

        forms = virtual_book_Form(request.POST)

        if forms.is_valid():

            instance = forms.save(commit=False)
            instance.user = request.user
            instance.save()

            return JsonResponse({'result' : True})

        else:

            print(forms.errors)

    else:


        return render(request, 'questions/virtual_book.html')










@login_required(login_url='login')
def company_llp_questions(request):

    print('dhdusdsudgusgdshdsygdb')
    print('dhdusdsudgusgdshdsygdb')
    print('dhdusdsudgusgdshdsygdb')
    print('dhdusdsudgusgdshdsygdb')
    print('dhdusdsudgusgdshdsygdb')


    print(request.POST)
    

    if request.method == 'POST':

        

        date_time = request.POST.get('date_time')

        
        d = dateutil.parser.parse(date_time)
        from_date_time = d.strftime("%Y-%m-%d %H:%M:%S")

        post = request.POST.copy() 
        post.update({"date_time" : from_date_time})
        request.POST = post

        forms = company_llp_Form(request.POST)

        if forms.is_valid():

            instance = forms.save(commit=False)
            instance.user = request.user
            instance.save()

            return JsonResponse({'result' : True})

        else:

            print(forms.errors)

    else:


        return render(request, 'questions/compny_llp.html')





import dateutil.parser

def submit(request):



    date_time = request.POST.get('date_time')

    
    d = dateutil.parser.parse(date_time)
    from_date_time = d.strftime("%Y-%m-%d %H:%M:%S")

        
    post = request.POST.copy() 
    post.update({"date_time" : from_date_time})
    request.POST = post



    forms = enquire_Form(request.POST)

    if forms.is_valid():

        instance = forms.save(commit=False)
        instance.user = request.user
        instance.save()

        return JsonResponse({'result' : True})

    

    else:

        print(forms.errors)

    

def refund_status(request):


    if request.method == "POST":


        

        date_time = request.POST.get('date_time')

        
        d = dateutil.parser.parse(date_time)
        from_date_time = d.strftime("%Y-%m-%d %H:%M:%S")

            
        post = request.POST.copy() 
        post.update({"date_time" : from_date_time})
        request.POST = post



        forms = refund_status_Form(request.POST)

        if forms.is_valid():

            print('save')

            forms.save()

            return redirect('index')

        

        else:

            
            print(forms.errors)
            print('forms.errors')

            return redirect('index')

    
    



def pricing(request):

    return render(request, 'pricing.html')



@login_required(login_url='login')
def unlock_eca(request):

    if request.method == "POST":

  

        date_time = request.POST.get('date_time')

        
        d = dateutil.parser.parse(date_time)
        from_date_time = d.strftime("%Y-%m-%d %H:%M:%S")

            
        post = request.POST.copy() 
        post.update({"date_time" : from_date_time})
        request.POST = post






        forms = unlock_eca_Form(request.POST)

        if forms.is_valid():

            instance = forms.save(commit=False)
            instance.user = request.user
            instance.save()

            return JsonResponse({'result' : True})



        

        else:

            print(forms.errors)

            return redirect('index')







@login_required(login_url='login')
def file_yourself_view(request):

    if request.method == "POST":


        print('iin hereeeeeeeeeeee')
    
          

        date_time = request.POST.get('date_time')

        
        d = dateutil.parser.parse(date_time)
        from_date_time = d.strftime("%Y-%m-%d %H:%M:%S")

            
        post = request.POST.copy() 
        post.update({"date_time" : from_date_time})
        request.POST = post



        

        forms = file_yourself_Form(request.POST)

        if forms.is_valid():

            instance = forms.save(commit=False)
            instance.user = request.user
            instance.save()
            print('done')

            return render(request, 'index.html', {'showmodal' : 'sdsd'})

        else:

            print(forms.errors)


    else:

        print('-------------------')
        print('-------------------')




@login_required(login_url='login')
@csrf_exempt
def prices_enquire_view(request):


    
    if request.method == 'POST':

        

        date_time = request.POST.get('date_time')

        
        d = dateutil.parser.parse(date_time)
        from_date_time = d.strftime("%Y-%m-%d %H:%M:%S")

        post = request.POST.copy() 
        post.update({"date_time" : from_date_time})
        request.POST = post

        forms = prices_enquire_Form(request.POST)

        if forms.is_valid():

            instance = forms.save(commit=False)
            instance.user = request.user
            instance.save()

            return JsonResponse({'result' : True})

        else:

            print(forms.errors)

    else:


        return render(request, 'pricing.html')





def submit_services_request(request):


    

    date_time = request.POST.get('date_time')

    
    d = dateutil.parser.parse(date_time)
    from_date_time = d.strftime("%Y-%m-%d %H:%M:%S")

        
    post = request.POST.copy() 
    post.update({"date_time" : from_date_time})
    request.POST = post



    forms = services_Form(request.POST)

    if forms.is_valid():

       forms.save()

       return JsonResponse({'result' : True})

    

    else:

        print(forms.errors)



def privacy_policy(request):

    return render(request, 'privacy-policy.html')

def contact_view(request):

    if request.method == "POST":

        print(request.POST)
        

        forms = contact_Form(request.POST)

        if forms.is_valid():
            
            print(  '--------------------------')

            forms.save()

            print('done')

            msg = "Request Send Successfully"

            return redirect(request, 'contact-us.html', {'msg' : msg})
        
        else:
                
            print(  '--------------------------')
            print(  '--------------------------')
            print(forms.errors)

    else:

        print(  '--------------------------')
        print(  '--------------------------')
        print(  '--------------------------')
        print(  '--------------------------')
        print(  '--------------------------')

        return render(request, 'contact-us.html')

def terms_condition(request):

    return render(request, 'terms-condition.html')

def admin_view(request):

    return render(request, 'admin-list-options.html')


def Income_From_House_Propety(request):

    return render(request, 'knowledge/Income From House Propety.html')


def Income_From_Busines_Profession(request):

    return render(request, 'knowledge/Income From Busines Profession.html')

def Income_From_Propery_Gain(request):

    return render(request, 'knowledge/Income From Propery Gain.html')



def Income_From_Salary(request):

    return render(request, 'knowledge/Income From Salary.html')


def Income_From_Other_Source(request):

    return render(request, 'knowledge/Income From Other Source.html')


def Avoid_Tax_Notices(request):

    return render(request, 'knowledge/Avoid Tax Notices.html')



def Tax_Deductions_At_Sources_TDS(request):

    return render(request, 'knowledge/Tax_Deductions_At_Sources_TDS.html')



def Tax_Collection_At_Sources_TCS(request):

    return render(request, 'knowledge/Tax_Collection_At_Sources_TCS.html')

def Due_Dates(request):

    return render(request, 'knowledge/Due_Dates.html')


