from django.contrib import admin
from .models import Photo
# Register your models here.

class PhotoAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'image_tag',
        'location',
        'updated_at',
    )
    readonly_fields=('image_tag',)
admin.site.register(Photo,PhotoAdmin)