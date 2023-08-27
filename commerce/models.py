from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    USER_TYPES = (
        ('Seller', 'Seller'),
        ('Buyer', 'Buyer')
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPES)

    def __str__(self):
        return self.username
    

class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(default=None, null=True)
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=11, decimal_places=0)
    image = models.ImageField(default=None, null=True)
    seller = models.ForeignKey(CustomUser, related_name='products', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

