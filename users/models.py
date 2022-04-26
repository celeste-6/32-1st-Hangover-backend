from django.db import models

from core.models import TimeStampedModel
from products.models import Product

class User(TimeStampedModel):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email    = models.EmailField(max_length=50,unique=True)
    password = models.CharField(max_length=200)
    friend   = models.ManyToManyField('self', through='Friend', symmetrical=False)
    cart     = models.ManyToManyField(Product, through='Cart')

    class Meta:
        db_table ='users'

class Cart(TimeStampedModel):
    user    = models.ForeignKey('User', on_delete=models.CASCADE,related_name='prebuyer')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count   = models.IntegerField()

class Friend(TimeStampedModel):
    friend_from = models.ForeignKey('User', on_delete=models.CASCADE, related_name='friend_from')
    friend_to   = models.ForeignKey('User', on_delete=models.CASCADE, related_name='friend_to')

    class Meta:
        db_table ='friends'