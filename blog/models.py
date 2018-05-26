from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=60)
    data_publicado = models.DateTimeField()
    imagem = models.ImageField(upload_to='imagens/')
    body= models.TextField(max_length=200)

    def summary(self):
        return self.body[:88]

    def data_ano(self):
        return self.data_publicado.strftime('%b %e %Y')
 