from django.db import models
from django.utils.translation import gettext as _
from settings.models import Country, City
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from utils.code import generaste_code

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name=_("User"), on_delete=models.CASCADE, related_name='user_profile')
    image = models.ImageField(_("Image"), upload_to='profile/')
    code = models.CharField(_("Code"), max_length=8, default=generaste_code)
    code_used = models.BooleanField(_("Code Used"), default=False)
    def __str__(self):
        return str(self.user.username)

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
@receiver(post_save, sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)

DATE_TYPE = (
    ('Home','Home'),
    ('Office','Office'),
    ('Bussines','Bussines'),
    ('Academy','Academy'),
    ('Others','Others'),
)
class UserPhoneNumber(models.Model):
    user = models.ForeignKey(User, verbose_name=_("User"), on_delete=models.CASCADE, related_name='user_phone')
    phone_number = models.CharField(_("Phone Number"), max_length=50)
    type = models.CharField(_("Type"), max_length=50, choices=DATE_TYPE)
    def __str__(self):
        return f"{self.user.username} - {self.type}"

    class Meta:
        verbose_name = 'UserPhoneNumber'
        verbose_name_plural = 'UserPhoneNumbers'


class UserAddress(models.Model):
    user = models.ForeignKey(User, verbose_name=_("User"), on_delete=models.CASCADE, related_name='user_address')
    type = models.CharField(_("Type"), max_length=50, choices=DATE_TYPE)
    country = models.ForeignKey(Country, verbose_name=_("Country"), on_delete=models.SET_NULL, null=True, related_name='user_country')
    city = models.ForeignKey(City, verbose_name=_("City"), on_delete=models.SET_NULL, null=True, related_name='user_city')
    notes = models.TextField(_("Notes"), max_length=1000, null=True, blank=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.type}"

    class Meta:
        verbose_name = 'UserAddress'
        verbose_name_plural = 'UserAddresss'
