from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=60)
    imagem = models.ImageField(upload_to='imagens/')
    description = models.CharField(max_length=200)
