from django.db import models
from django.db.models import Model
from django.contrib.auth.models import User

# Create your models here.

CATEGORY = (
    ('Mobiles','Mobiles'),
    ('MobilesAcc','MobilesAcc'),
    ('Earphones','Earphones'),
)

class Product(models.Model):
    name = models.CharField(max_length = 100,null=True)
    category = models.CharField(max_length = 100,choices = CATEGORY)
    quantity = models.PositiveIntegerField(null=True)

    class Meta:
        verbose_name_plural = 'Products'

    def __str__(self):
        return f'{self.name}-{self.quantity}'

class Order(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,null = True)
    staff = models.ForeignKey(User,models.CASCADE,null = True)
    order_quantity = models.PositiveIntegerField(null = True)
    date = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name_plural = 'Order'

   