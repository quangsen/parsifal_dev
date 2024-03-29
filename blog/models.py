from django.db import models
from django.contrib.auth.models import User

class Entry(models.Model):
    DRAFT = 'D'
    HIDDEN = 'H'
    PUBLISHED = 'P'
    ENTRY_STATUS = (
        (DRAFT, 'Draft'),
        (HIDDEN, 'Hidden'),
        (PUBLISHED, 'Published'),
    )

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, null=True, blank=True)
    content = models.TextField(max_length=4000, null=True, blank=True)
    summary = models.TextField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=10, choices=ENTRY_STATUS)
    start_publication = models.DateTimeField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    edited_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="+")
