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
    slug = models.SlugField()
    description = models.TextField()
    image = models.ImageField()
    seller = models.ForeignKey(CustomUser, on_delete=models.PROTECT)

