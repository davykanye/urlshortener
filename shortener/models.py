from django.db import models

# Create your models here.

class ShortUrl(models.Model):
    slug = models.SlugField(max_length=30, blank=True, null=False)
    url = models.URLField(max_length = 200)

    def __str__(self):
        return self.name