from django.http import HttpRequest
from django.shortcuts import render

# Create your views here.
def blog(request):
    return render(request,'Blogs/index.html')