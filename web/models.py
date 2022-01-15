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
    

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ('-id',)
        verbose_name = _('Gallery')
        verbose_name_plural = _('Galleries')

class ImageUpload(models.Model):
    gallery = models.ForeignKey(Gallery,on_delete=models.CASCADE,related_name="gallery")
    image = models.ImageField(upload_to="web/Gallery/")

    class Meta:
        ordering = ('-id',)



class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(max_length=120)
    phone = models.CharField(max_length=120,blank=True,null=True)
    message = models.TextField()

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ('id',)
        verbose_name = _('Message')
        verbose_name_plural = _('Messages')