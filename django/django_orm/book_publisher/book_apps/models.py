from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Publisher(models.Model):
    name = models.CharField(max_length=255)
    books = models.ManyToManyField(Book, related_name="publishers")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
