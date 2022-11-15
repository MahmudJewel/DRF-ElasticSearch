from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
# Create your views here.

def home(request):
    return HttpResponse('Home page')