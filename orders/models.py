from django.db import models

from core.models import TimeStampedModel
from users.models import User
from products.models import Product

class Order(TimeStampedModel):
    order_number = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.ForeignKey('OrderStatus', on_delete=models.CASCADE)

    class Meta:
        db_table ='orders'

class OrderItems(TimeStampedModel):
    order_id = models.ForeignKey('Order', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_item_status = models.ForeignKey('OrderItemStatus', on_delete=models.CASCADE)
    shipment_id = models.ForeignKey('OrderShipment', on_delete=models.CASCADE, null=True)

    class Meta:
        db_table ='orderitems'

class OrderStatus(TimeStampedModel):
    status = models.CharField(max_length=50)

    class Meta:
        db_table ='orderstatuses'

class OrderItemStatus(TimeStampedModel):
    status = models.CharField(max_length=50)

    class Meta:
        db_table ='orderitemstatuses'

class OrderShipment(TimeStampedModel):
    tracking_number = models.CharField(max_length=200)
    delivery_company = models.CharField(max_length=200)

    class Meta:
        db_table ='ordershipments'