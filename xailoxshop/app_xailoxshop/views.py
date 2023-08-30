from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import xailox
from .forms import AdvForm
from django.urls import reverse,reverse_lazy
from django.contrib.auth.decorators import login_required

def index(request):
    xailoxs = xailox.objects.all()
    context = {'xailoxs' : xailoxs}
    return render(request, 'app_xailox/index.html', context)


def top_sellers(request):
    return render(request, 'app_xailox/top-sellers.html')

@login_required(login_url=reverse_lazy('login'))
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
    return render(request, 'app_xailox/advertisement-post.html',context)

def register(request):
    return render(request, 'app_auth/register.html')

def login(request):
    return render(request, 'app_auth/login.html')

def profile(request):
    return render(request, 'app_auth/profile.html')

