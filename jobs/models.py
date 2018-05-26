from django.db import models
#jobs area (herdando de models) 

class Job(models.Model):
    image = models.ImageField(upload_to='imagens/')
    sumary = models.CharField(max_length=200)
