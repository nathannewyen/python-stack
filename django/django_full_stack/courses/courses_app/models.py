from django.db import models

# Create your models here.


class CourseManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if len(postData["name"]) < 1:
            errors["error_name"] = "Please enter course name ( > 5 characters )"
        elif len(postData["name"]) < 5:
            errors["error_name"] = "Please enter course name more than 5 characters"
        if len(postData["description"]) < 1:
            errors["error_description"] = "Please enter description ( > 15 characters )"
        elif len(postData["description"]) < 15:
            errors["error_description"] = "Please enter description more than 15 characters"
        return errors


class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    date = models.DateField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()
