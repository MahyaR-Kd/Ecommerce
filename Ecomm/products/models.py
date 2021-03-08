from django.db import models
from django.utils import timezone
# Create your models here.

class Product(models.Model):
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Published'),
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=10, unique=True)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='images')
    price =  models.DecimalField(max_digits=6,decimal_places=0)
    publish = models.TimeField(default=timezone.now)
    created = models.TimeField(auto_now=True)
    updated = models.TimeField(auto_now_add=True)
    status = models.CharField(max_length=1,choices=STATUS_CHOICES)
    def __str__(self):
        return self.title