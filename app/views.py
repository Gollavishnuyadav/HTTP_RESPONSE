from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def one(request):
    return HttpResponse("good")