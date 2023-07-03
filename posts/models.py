from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=36)



    def __str__(self):
        return self.title

class Product(models.Model):
    name_of_product = models.CharField(max_length=256)
    image_of_product = models.ImageField()
    measure_of_product = models.CharField(max_length=10)
    amount_of_product = models.IntegerField(default=0)
    cost_of_product = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category)
    description = models.TextField()


    def __str__(self):
        return self.name_of_product


    @property
    def categories_list(self) -> list:
        return self.categories.all()



