from django.db import models
from datetime import datetime
from django.template.defaultfilters import slugify
import random
# Create your models here.

class SiteSettings(models.Model):
    name= models.CharField(max_length=256)
    title= models.CharField(max_length=256)
    slug= models.CharField(max_length=256)
    description= models.TextField()
    photo = models.ImageField(upload_to="site_photos")
    is_active = models.BooleanField()
    category= models.CharField(max_length=256)
    modified = models.DateTimeField(datetime.now())
    def save(self, *args, **kwargs):
        string = "%s-%s" % (random.randrange(0, 101, 2), self.name)
        self.slug = slugify(string)
        super(SiteSettings, self).save(*args, **kwargs)