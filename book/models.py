from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=50, unique=True)
    description = models.TextField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
