from django.db import models

# Create your models here.

class Movie(models.Model):

   year=models.IntegerField()
   desc=models.TextField()
   img=models.ImageField(upload_to='gallery')


   def __str__(self):
      return self.name
