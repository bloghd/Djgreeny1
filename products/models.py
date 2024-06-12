from django.db import models
from django.utils.translation import gettext as _

# Create your models here.

class Product(models.Model):
    name = models.CharField(_("Name"), max_length=100)
    sku = models.IntegerField(_("SKU"))
    brand = models.ForeignKey("Brand", verbose_name=_("Brand"), on_delete=models.SET_NULL, null=True, blank=True)
    price = models.FloatField(_("Price"))
    desc = models.TextField(_("Descrption"), max_length=10000)

    

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("s")

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(_("Name"), max_length=50)

    class Meta:
        verbose_name = _("Brand")
        verbose_name_plural = _("s")

    def __str__(self):
        return self.name

