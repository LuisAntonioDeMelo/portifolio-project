from django.http import HttpRequest
from django.shortcuts import render
from .models  import Blog

# Create your views here.
def mainblog(request):
    blogs = Blog.objects
    return render(request,'Blogs/mainblog.html',{'blogs':blogs})