from django.db import models
from django.utils.safestring import mark_safe
# Create your models here.
class Photo(models.Model):
    title   = models.CharField(max_length=20)
    location = models.CharField(max_length=30)
    image   = models.ImageField(blank=False)
    updated_at  = models.DateTimeField(auto_now_add=True)
    def image_tag(self):
        if self.image:
            print(self.image.url + " JPJP")
            return mark_safe('<img src="%s" width=60/>' % self.image.url )
        else:
            return 'No found image'
    
    def __str__(self):
        return self.title
