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

class Customer(models.Model):
    first_name = models.CharField(max_length=50,null=True)
    last_name = models.CharField(max_length=50,null=True)
    phone = models.CharField(max_length=15,null=True)
    email = models.EmailField(max_length=50,null=True) # method 1 unique=True
    password = models.CharField(max_length=500,null=True)

    def register(self):
        self.save()

    def __str__(self):
        return self.email

    @staticmethod
    def getCustomer(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False

    def isExists(self):# method 2 to keep email unique, not working method 3 is implemented in views.py 
        if Customer.objects.filter(email=self.email):
            return True
        
        return False

