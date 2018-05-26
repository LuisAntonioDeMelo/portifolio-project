from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=60)
    data_publicado = models.DateTimeField()
    imagem = models.ImageField(upload_to='imagens/')
    body= models.TextField(max_length=200)
