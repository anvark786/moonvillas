from django.db import models
from django.utils.translation import gettext_lazy as _


class Gallery(models.Model):
    CATEGORY_CHOICES = (
    ('bedroom', 'Bedroom'),    
    ('drawing', 'Drawing Room'),
    ('living', 'Living Room'),
    ('kitchen', 'Kitchen'),
    ('garage', 'Garage'),
    ('basement', 'Basement'),
    )
    category = models.CharField(max_length=40, choices=CATEGORY_CHOICES,blank=True,null=True)

    image = models.ImageField(upload_to="web/Gallery/")

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ('id',)
        verbose_name = _('Gallery')
        verbose_name_plural = _('Galleries')


class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(max_length=120)
    message = models.TextField()

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ('id',)