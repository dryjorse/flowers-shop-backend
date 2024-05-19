from django.contrib import admin
from .models import Flower, Image

class ImageInline(admin.TabularInline):
    model = Image
    extra = 1  

class FlowerAdmin(admin.ModelAdmin):
    inlines = [ImageInline]

admin.site.register(Flower, FlowerAdmin)
