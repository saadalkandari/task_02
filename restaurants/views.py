from django.shortcuts import render
from django.http import HttpResponse    



def hello_world(request):
    return  HttpResponse("restaurants.html",{"msg":"Hello World!"})

