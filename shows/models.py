from django.db import models
from datetime import datetime


class ShowManager(models.Manager):
    def basic_validator(self, formData):
        errors = {}
        if len(formData['title']) < 2:
            errors["title"] = "Show title should be at least 3 characters"
        if len(formData['network']) < 3:
            errors["network"] = "Network should be at least 3 characters"
        if formData['desc'] != '' and len(formData['desc']) < 10:
            errors['desc'] = "Description should be at least 10 characters"
        if datetime.strptime(formData['reldate'], '%Y-%m-%d') > datetime.now():
            errors['reldate'] = "Release Date should be in the past"
        return errors

class Shows(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField(auto_now=False)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()

