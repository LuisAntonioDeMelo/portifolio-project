from django.urls import path
from . import views 

urlpatterns =[
    path('',views.mainblog, name='mainblogs' ),
    path('<int:blog_id>/',views.detail, name='detail'),
]