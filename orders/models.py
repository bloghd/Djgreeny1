from django.db import models
from django.utils.translation import gettext as _
from django.utils import timezone
from products.models import Product
from utils.code import generaste_code
ORDER_STATUS = (
    ('Recieved','Recieved'),
    ('Processod','Processod'),
    ('Shipped','Shipped'),
    ('Deliverod','Deliverod'),
)


class Order(models.Model):
    code = models.CharField(_("Code"), max_length=8, default=generaste_code)
    oder_status= models.CharField(_("Order Status"), max_length=15, default=ORDER_STATUS)
    order_time = models.DateTimeField(_("Order Time"), default=timezone.now)
    delivery_time= models.DateTimeField(_("Delivery Time"), null=True, blank=True)

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")

    def __str__(self):
        return self.code

class OrderDetail(models.Model):
    order = models.ForeignKey(Order, verbose_name=_("Order"), related_name='order_detail',on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name=_("Product"), related_name='order_product',on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.FloatField(_("Quantity"))
    price = models.FloatField(_("Price"))

    class Meta:
        verbose_name = _("OrderDetail")
        verbose_name_plural = _("OrderDetails")

    def __str__(self):
        return str(self.order)

