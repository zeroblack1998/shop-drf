from django.db import models

class Product(models.Model):
    title = models.CharField("Name", max_length=240)
    discription = models.TextField()
    price = models.PositiveIntegerField()
    stack = models.PositiveIntegerField()

