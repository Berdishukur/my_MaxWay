from django.db import models

# Create your models here.
class Ctegory(models.Model):
    name=models.CharField(max_length=100,blank=False,null=False)
    created=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
