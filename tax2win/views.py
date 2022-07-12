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


    return render(request, 'index.html')

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

            forms.save()

            return JsonResponse({'result' : True})

        else:

            print(forms.errors)


    else:

        return render(request, 'questions/direct_taxation.html')

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

            forms.save()

            return JsonResponse({'result' : True})

        else:

            print(forms.errors)

    else:

        return render(request, 'questions/indirect_taxation.html')

def virtual_book_questions(request):


    
    if request.method == 'POST':

        

        date_time = request.POST.get('date_time')

        
        d = dateutil.parser.parse(date_time)
        from_date_time = d.strftime("%Y-%m-%d %H:%M:%S")

        post = request.POST.copy() 
        post.update({"date_time" : from_date_time})
        request.POST = post

        forms = virtual_book_questions_Form(request.POST)

        if forms.is_valid():

            forms.save()

            return JsonResponse({'result' : True})

        else:

            print(forms.errors)

    else:


        return render(request, 'questions/virtual_book.html')

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

        forms = company_llp_questions_Form(request.POST)

        if forms.is_valid():

            forms.save()

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

       forms.save()

       return JsonResponse({'result' : True})

    

    else:

        print(forms.errors)

    

def refund_status(request):


    

    date_time = request.POST.get('date_time')

    
    d = dateutil.parser.parse(date_time)
    from_date_time = d.strftime("%Y-%m-%d %H:%M:%S")

        
    post = request.POST.copy() 
    post.update({"date_time" : from_date_time})
    request.POST = post



    forms = refund_status_Form(request.POST)

    if forms.is_valid():

       forms.save()

       return JsonResponse({'result' : True})

    

    else:

        print(forms.errors)
    








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

def terms_condition(request):

    return render(request, 'terms-condition.html')