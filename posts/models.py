from django.db import models


class Product(models.Model):
    name_of_product = models.CharField(max_length=256)
    image_of_product = models.ImageField()
    measure_of_product = models.CharField(max_length=10)
    amount_of_product = models.IntegerField(default=0)
    cost_of_product = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now_add=True)

