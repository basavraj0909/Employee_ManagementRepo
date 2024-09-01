from django.db import models
from django.utils import timezone


class Blog(models.Model):
    title = models.CharField(max_length=60)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now())
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
