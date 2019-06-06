from django.db import models

class Profile(models.Model):
    public_email = models.EmailField()
    location = models.CharField(max_length=50)
    user = models.CharField(max_length=50)