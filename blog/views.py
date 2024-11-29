from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.

class HomePage(TemplateView): 
    """
    Displays home page"
    """
    template_name = 'base.html'
    

def my_blog(request):
    return HttpResponse("<h1>This is my blog!<h1>")
