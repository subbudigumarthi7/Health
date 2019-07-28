from django.contrib.auth import authenticate, login as auth_login, login

from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
import happx
from happx.forms import UserForm, Proform


def base(request):
    return render(request,'happx/base.html')
def index(request):
    return render(request,'happx/index.html')

def about(request):
    return render(request,'happx/about.html')

def register(request):
    # if this is a POST request we need to process the form data
    template = 'happx/register.html'

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UserForm(request.POST)
        # check whether it's valid:
        if form.is_valid():

            if User.objects.filter(username=form.cleaned_data['username']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Username already exists.'
                })
            elif User.objects.filter(email=form.cleaned_data['email']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Email already exists.'
                })
            elif form.cleaned_data['password'] != form.cleaned_data['confirm_password']:
                return render(request, template, {
                    'form': form,
                    'error_message': 'Passwords do not match.'
                })
            else:
                # Create the user:
                user = User.objects.create_user(
                    form.cleaned_data['username'],
                    form.cleaned_data['email'],
                    form.cleaned_data['password']
                )

                user.save()
                # redirect to accounts page:
                return HttpResponseRedirect('/happx/base')

    # No post data availabe, let's just show the page.
    else:
        form = UserForm()
    return render(request, template, {'form': form})


def auth_login(request):
    if request.method == 'POST':
        form=UserForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        # Check username and password combination if correct
        user = authenticate(username=username, password=password)
        if user is not None:
            # Save session as cookie to login the user
            login(request, user)

            # Success, now let's login the user.
            return HttpResponseRedirect('/happx/pro')
        else:
            # Incorrect credentials, let's throw an error to the screen.
            return render(request, 'happx/login.html',
                          {'error_message': 'Incorrect username and / or password.'})
    else:
        form=UserForm()
        return render(request, 'happx/login.html',{'form':form})


def submit(request):

        return render(request,'happx/submit.html')








def smart(request):
    return render(request,'happx/smart.html')


def contact(request):
    return render(request,'happx/contact.html')


def logout(request):
    return render(request,'happx/index.html')


def pro(self,request):
    pform=Proform(request.POST)
    if pform.is_valid():
       pform.save()
       return render(request,'happx/submit.html')
    else:
         pform=Proform()
    return render(request,'happx/pro.html',{'pform':pform})