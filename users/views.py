from email import message
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from tax2win.models import *



from .forms import *


def login_page(request):
    forms = LoginForm()
    if request.method == 'POST':




        print('in')

    
        print('1')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        print('2')

        

        
        if user:
            print('yes')
            login(request, user)


            if user.is_superuser:

                return redirect('admin-index')

            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            return redirect('index')

        else:

            print('----------------')

            msg = 'Credentials wrong'

            print('not done')
            print(forms.errors)
            print('---------------------------')


            context = {
                'msg': msg,
                'form': forms,
            }
            return render(request, 'users/login.html', context)
    
        
    
    return render(request, 'users/login.html')



def register_page(request):

    forms = registerForm()
    if request.method == 'POST':
        print('1')
        forms = registerForm(request.POST)
        if forms.is_valid():
            print('2')

            email = forms.cleaned_data['email']
            password = forms.cleaned_data['password1']
            user = authenticate(email=email, password=password)
            print('3')

            if user:
                
                messages.error(request, 'user already exsist')
                messages.success(request, 'sdst')
                print('done')
                return redirect('register')
            else:
                forms.save()
                
                return redirect('login')
        else:

            print(forms.errors)

            context = {
                'form': forms,
            }

            return render(request, 'users/register.html', context)

    else:
        print(forms.as_p)

        context = {'form': forms}

        return render(request, 'users/register.html', context)



def logout_page(request):
    print('in logit')
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def your_requests(request):

    direct_tax = direct_taxcation.objects.filter(user = request.user)
    indirect_tax = indirect_taxcation.objects.filter(user = request.user)
    company_tax = company_llp_questions.objects.filter(user = request.user)
    virtual_tax = virtual_book_questions.objects.filter(user = request.user)
    print(direct_tax)
    context = {
        'direct_tax' : direct_tax,
        'indirect_tax' : indirect_tax,
        'company_tax' : company_tax,
        'virtual_tax' : virtual_tax,
    }


    return render(request, 'users/accounts.html', context)

