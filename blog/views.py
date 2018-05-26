from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404
from .models  import Blog

# Create your views here.
def mainblog(request):
    blogs = Blog.objects
    return render(request,'Blogs/mainblog.html',{'blogs':blogs})
#post blog 
def detail(request,blog_id):
    blog_detail = get_object_or_404(Blog,pk=blog_id)
    return render(request,'Blogs/detail.html',{'details':blog_detail})