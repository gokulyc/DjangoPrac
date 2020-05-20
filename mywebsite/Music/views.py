# from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string

# Create your views here.

# Class based view
# Def method based views

def Home(request):
    return HttpResponse(render_to_string("index.html"))