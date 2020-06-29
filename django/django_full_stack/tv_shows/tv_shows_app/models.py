from django.db import models
import datetime

# Create your models here.


class ShowManager(models.Manager):
    def basic_validator(self, postData):
        current_date = datetime.date.today()
        errors = {}
        print(current_date)
        print(postData)
        # add keys and values to errors dictionary for each invalid field
        if len(postData['title']) < 3:
            errors["title"] = "Show title should be at least 2 characters"
        if len(postData['network']) < 2:
            errors["network"] = "Show network should be at least 3 characters"
        if postData["release_date"] >= f"{current_date}":
            if len(postData["description"]) < 10:
                errors["descripion"] = "Show description must be 10 characters because you pick release date is current time. This show is must be new and we need more scription about it"
        return errors


class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField(null=True)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()
