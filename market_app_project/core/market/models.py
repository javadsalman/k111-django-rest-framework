from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=50)
    price = models.FloatField()
    code = models.CharField(max_length=20, unique=True)
    expire = models.DateField()
    created = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    
class Statistic(models.Model):
    count = models.IntegerField()
    gain = models.FloatField()