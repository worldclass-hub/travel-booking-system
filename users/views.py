
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.http import HttpResponse




def home(request):
    return render(request, 'travel/home.html')




def about(request):
    return render(request, 'travel/about.html')


def offers(request):
    return render(request, 'travel/offers.html')


def news(request):
    return render(request, 'travel/news.html')


def contact(request):
    return render(request, 'travel/contact.html')


# Create your views here.

def user_login(request):
    return HttpResponse("User Login Page")


def user_logout(request):
    logout(request)
    return redirect('/')  # Redirect to home page after logout



def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after registration
            messages.success(request, "Registration successful!")
            return redirect('/')  # Redirect to home page
    else:
        form = UserCreationForm()
    
    return render(request, 'users/register.html', {'form': form})




@login_required
def user_profile(request):
    return render(request, 'users/profile.html')
