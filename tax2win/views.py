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

def questions(request):


    return render(request, 'questions.html')





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

    

