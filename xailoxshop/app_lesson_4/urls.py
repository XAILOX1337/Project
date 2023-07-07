from django.urls import path
from . import views 
urlpatterns = [path('',views.index),
               path('lesson_4',views.lesson_4)]