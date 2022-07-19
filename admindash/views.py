from django.shortcuts import redirect, render
from tax2win.models import *
from tax2win.forms import *
import dateutil.parser


# Create your views here.



def index(request):

    return render(request, 'admin-templates/index.html')

def admin_direct_tax(request):

    data = direct_taxcation.objects.all()

    return render(request, 'admin-templates/admin_direct_tax.html', {'data' : data})

def admin_indirect_tax(request):

    data = indirect_taxcation.objects.all()

    return render(request, 'admin-templates/admin_indirect_tax.html', {'data' : data})

def admin_company(request):

    data = company_llp_questions.objects.all()

    return render(request, 'admin-templates/admin_company.html', {'data' : data})

def admin_virtual(request):

    data = virtual_book_questions.objects.all()

    return render(request, 'admin-templates/admin_virtual.html', {'data' : data})


def update_direct_tax(request, request_id):

    if request.method == "POST":

        print(request.POST)

        instance = direct_taxcation.objects.get(id = request_id)
        
       
        date_time = request.POST.get('date_time')

        
        d = dateutil.parser.parse(date_time)
        from_date_time = d.strftime("%Y-%m-%d %H:%M:%S")

        post = request.POST.copy() 
        post.update({"date_time" : from_date_time})
        request.POST = post


        form = direct_taxcation_Form(request.POST, instance = instance)


        if form.is_valid():

            form.save()

            return redirect('admin_direct_tax')

        else:

            print(form.errors)

    else:
        print('------------------------------------')

        instance = direct_taxcation.objects.get(id = request_id)
        print(instance)
        print(instance.comment)

        form = direct_taxcation_Form(instance = instance)

        print(form)

        return render(request, 'admin-templates/update_direct_tax.html', {'form' : form})


def update_indirect_tax(request, request_id):

    if request.method == "POST":

        instance = indirect_taxcation.objects.get(id = request_id)

        date_time = request.POST.get('date_time')

        
        d = dateutil.parser.parse(date_time)
        from_date_time = d.strftime("%Y-%m-%d %H:%M:%S")

        post = request.POST.copy() 
        post.update({"date_time" : from_date_time})
        request.POST = post

        form = indirect_taxcation_Form(request.POST, instance = instance)

        if form.is_valid():

            form.save()

            return redirect('admin_indirect_tax')

        else:

            print(form.errors)

    else:

        instance = indirect_taxcation.objects.get(id = request_id)

        form = indirect_taxcation_Form(instance = instance)

        return render(request, 'admin-templates/update_indirect.html', {'form' : form})


def update_comapny_tax(request, request_id):

    if request.method == "POST":

        instance = company_llp_questions.objects.get(id = request_id)

        date_time = request.POST.get('date_time')

        
        d = dateutil.parser.parse(date_time)
        from_date_time = d.strftime("%Y-%m-%d %H:%M:%S")

        post = request.POST.copy() 
        post.update({"date_time" : from_date_time})
        request.POST = post

        form = company_llp_Form(request.POST, instance = instance)

        if form.is_valid():

            form.save()

            return redirect('admin_company')

        else:

            print(form.errors)

    else:

        instance = company_llp_questions.objects.get(id = request_id)

        form = company_llp_Form(instance = instance)


        return render(request, 'admin-templates/update_company_tax.html', {'form' : form})


def update_virtual_tax(request, request_id):

    if request.method == "POST":

        instance = virtual_book_questions.objects.get(id = request_id)

        date_time = request.POST.get('date_time')

        
        d = dateutil.parser.parse(date_time)
        from_date_time = d.strftime("%Y-%m-%d %H:%M:%S")

        post = request.POST.copy() 
        post.update({"date_time" : from_date_time})
        request.POST = post

        form = virtual_book_Form(request.POST, instance = instance)

        if form.is_valid():

            form.save()

            return redirect('admin_virtual')

        else:

            print(form.errors)

    else:

        instance = virtual_book_questions.objects.get(id = request_id)

        form = virtual_book_Form(instance = instance)

        return render(request, 'admin-templates/update_virtual_tax.html', {'form' : form})


def delete_direct_tax(request, request_id):


    direct_taxcation.objects.get(id = request_id).delete()
        
    return redirect('admin_direct_tax')

def delete_indirect_tax(request, request_id):

    indirect_taxcation.objects.get(id = request_id).delete()

    return redirect('admin_indirect_tax')

def delete_comapny_tax(request, request_id):

   
    company_llp_questions.objects.get(id = request_id).delete()

    return redirect('admin_company')


def delete_virtual_tax(request, request_id):

    virtual_book_questions.objects.get(id = request_id).delete()

    return redirect('admin_virtual')

