from django.contrib import admin
from .models import Gallery,Contact


class GalleryAdmin(admin.ModelAdmin):
	list_display = ('id','category','image',)
admin.site.register(Gallery,GalleryAdmin)

class ContactAdmin(admin.ModelAdmin):
	list_display = ('id','name','message',)
admin.site.register(Contact,ContactAdmin)