from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import views as auth_view
from pages.forms import SignUpForm

# Create your views here.
def home(request):
    return render(request, 'index.html')

def signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        print('post request')
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form':form})
    

