from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
from taggit.managers import TaggableManager

# Create your models here.
FLAG_TYPE =(
    ('New','New',),
    ('Feature','Feature'),
)

RATE =(
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),

)

class Product(models.Model):
    name = models.CharField(_("Name"), max_length=100)
    sku = models.IntegerField(_("SKU"))
    brand = models.ForeignKey("Brand", verbose_name=_("Brand"), related_name='product_brand',on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey("Category", verbose_name=_("Category"), related_name='product_category',on_delete=models.SET_NULL, null=True, blank=True)
    price = models.FloatField(_("Price"))
    tags = TaggableManager(blank=True)
    desc = models.TextField(_("Descrption"), max_length=10000)
    flag = models.CharField(_("Flag"), max_length=15, choices=FLAG_TYPE)
    slug = models.SlugField(_("Slug"), null=True, blank=True)

    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    image = models.ImageField(_("Image"), upload_to='Brand/')
    slug = models.SlugField(_("Slug"), null=True, blank=True)

    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Brand, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _("Brand")
        verbose_name_plural = _("Brands")

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    image = models.ImageField(_("Image"), upload_to='Category/')
    

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.name
    
class Review(models.Model):
    user = models.ForeignKey(User, verbose_name=_("User"), related_name='review_user',on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey(Product, verbose_name=_("Product"), related_name='product_review',on_delete=models.SET_NULL, null=True, blank=True)
    review = models.TextField(_("Review"), max_length=10000)
    rate = models.IntegerField(_("Rate"), choices=RATE)
    created_at = models.DateTimeField(_("Created_At"), default=timezone.now)
    

    class Meta:
        verbose_name = _("Review")
        verbose_name_plural = _("Reviews")

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"
    
class ProductImages(models.Model):
    product = models.ForeignKey(Product, verbose_name=_("Product"), related_name='product_image',on_delete=models.CASCADE)
    image = models.ImageField(_("Image"), upload_to='ProductImages/')
    

    class Meta:
        verbose_name = _("ProductImage")
        verbose_name_plural = _("ProductImages")

    def __str__(self):
        return str(self.product.name)






