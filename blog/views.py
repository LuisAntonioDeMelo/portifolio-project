from django.http import HttpRequest
from django.shortcuts import render

# Create your views here.
def blog(request):
    render(request,'index.html')