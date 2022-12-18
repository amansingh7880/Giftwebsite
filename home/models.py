from django.db import models
# Create your models here.
class Image(models.Model):
    title=models.CharField(max_length=150)
    image=models.ImageField(upload_to='media/Image/%Y/')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name