from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse('Successfull!')


def lesson_4(requets):
    return HttpResponse('Домашка по 4 занятию)')