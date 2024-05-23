from django.db import models

# Create your models here.
class Fruty(models.Model):
    full_name=models.CharField(max_length=100)
    photo=models.ImageField(upload_to='images')
    scientific_name=models.CharField(max_length=100)
    season_name=models.CharField(max_length=100)
    cost=models.CharField(max_length=100)
                            