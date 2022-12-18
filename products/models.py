from django.db import models
from django.conf import settings

# Create your models here.
class ProductItem(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    image=models.ImageField(upload_to='Images/')
    price = models.DecimalField(decimal_places=2, max_digits=20, default=39.99)
    summary = models.TextField(default='This is cool!')
    featured = models.BooleanField(default=False) # null=True, blank=True
    slug = models.SlugField(unique=True, null=True, blank=True)

    def get_absolute_url(self):
        return f"/products/{self.slug}/"

    def __str__(self):
        return self.title
