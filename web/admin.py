from django.contrib import admin
from .models import Gallery,Contact,ImageUpload



class ImageUploadInline(admin.StackedInline):
    model = ImageUpload


class GalleryAdmin(admin.ModelAdmin):
	inlines = [
        ImageUploadInline,
    ]
	list_display = ('id','category',)
admin.site.register(Gallery,GalleryAdmin)

class ContactAdmin(admin.ModelAdmin):
	list_display = ('id','name','email','phone','message',)
admin.site.register(Contact,ContactAdmin)