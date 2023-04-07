from django.urls import path, include
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "index.html")

urlpatterns = [
    path("", index, name="index"),
]
