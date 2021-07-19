from django.db import models
from django.db.models.fields import CharField, IntegerField
from django.db.models.fields.files import ImageField

# Create your models here.

class Product(models.Model):
    name = CharField(max_length=100,null=True)
    img = ImageField(null=True)
    price = IntegerField(default = 0,null=True)
    des = CharField(max_length=1000,null=True,default='Description')

    def __str__(self):
        return self.name