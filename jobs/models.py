from django.db import models
#jobs area (herdando de models) 
class Job(models.Model):
    imagefiles = models.ImageField(upload_to='imagens/')
    sumary = models.CharField(max_length=200)
