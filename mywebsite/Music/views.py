# from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string

# Create your views here.

# Class based view
# Def method based views

def Home(request):
    return HttpResponse(render_to_string("index.html"))

def Guitar(request):
    return HttpResponse(render_to_string("a/guitar.html"))

def Violin(request):
    return HttpResponse(render_to_string("a/violin.html"))
def Flute(request):
    return HttpResponse(render_to_string("a/flute.html"))
def Trumpet(request):
    return HttpResponse(render_to_string("a/trumpet.html"))
def Drums(request):
    return HttpResponse(render_to_string("a/drums.html"))