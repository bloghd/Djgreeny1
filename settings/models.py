from django.db import models
from django.utils.translation import gettext as _

# Create your models here.

class Country(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'

class City(models.Model):
    country = models.ForeignKey(Country, verbose_name=_("Country"), related_name='country_city',on_delete=models.CASCADE)
    name = models.CharField(_("Name"), max_length=50)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'


class Company(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    logo = models.ImageField(_("Logo"), upload_to='company/')
    about = models.TextField(_("About"), max_length=500)
    fa_link = models.URLField(_("Facebook"), max_length=200)
    tw_link = models.URLField(_("Tweiter"), max_length=200)
    ins_link = models.URLField(_("Instgarm"), max_length=200)
    email = models.EmailField(_("Email"), max_length=254)
    phone_number = models.CharField(_("Phone Number"), max_length=50)
    address = models.CharField(_("Address"), max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'