from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=256)

    def __str__(self):
        return str(self.category_name)


class Product(models.Model):
    product_name = models.CharField(max_length=512)
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_des = models.TextField(blank=True)
    product_price = models.FloatField()
    product_photo = models.ImageField(upload_to='media')
    product_amount = models.IntegerField()

    def __str__(self):
        return str(self.product_name)


