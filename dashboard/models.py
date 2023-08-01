from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=100,blank=False,null=False)
    created=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Product(models.Model):
    title=models.CharField(max_length=100,null=True,blank=True)
    descriptions=models.TextField(blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    created=models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    image = models.ImageField(upload_to='products')
    def __str__(self):
         return self.title





