from django.urls import path
from . import views 

urlpatterns =[
    path('',views.mainblog, name='mainblog' )
]