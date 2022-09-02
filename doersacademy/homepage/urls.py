from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.InsertDetails),
    path('form/',views.form),
    path('digital-content-masterclass/',views.course),
]