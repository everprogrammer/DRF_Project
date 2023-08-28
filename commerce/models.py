from django.db import models
from auth_app.models import CustomUser

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(default=None, null=True)
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=11, decimal_places=0)
    image = models.ImageField(default=None, null=True)
    seller = models.ForeignKey(CustomUser, related_name='products', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

