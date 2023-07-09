from django.db import models

# Create your models here.
class chocolate(models.Model):
    img=models.ImageField(upload_to='pic')
    title=models.CharField(max_length=50)
    price=models.CharField(max_length=50)

    def __str__(self):
         return self.title
    


    