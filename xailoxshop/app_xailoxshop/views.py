from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import xailox
from .forms import AdvForm
from django.urls import reverse

def index(request):
    xailoxs = xailox.objects.all()
    context = {'xailoxs' : xailoxs}
    return render(request, 'index.html', context)


def top_sellers(request):
    return render(request, 'top-sellers.html')

def advertisement_post(request):
    if request.method == 'POST':
        form = AdvForm(request.POST, request.FILES)
        if form.is_valid():
            advertisement = xailox(**form.cleaned_data)
            advertisement.user = request.user 
            advertisement.save()
            url = reverse('main-page')
            return redirect(url)
    else:
        form = AdvForm()
    context = {'form':form}
    return render(request, 'advertisement-post.html',context)

def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')

def profile(request):
    return render(request, 'profile.html')

