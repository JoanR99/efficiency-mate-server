from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=255, blank=True)
    content = models.TextField(blank=True)
    is_archived = models.BooleanField(default=False)
    is_pinned = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    colors = [
        ("white", "white"),
        ("red", "red"),
        ("yellow", "yellow"),
        ("orange", "orange"),
        ("blue", "blue"),
        ("teal", "teal"),
        ("green", "green"),
        ("purple", "purple"),
        ("pink", "pink"),
        ("gray", "gray"),
        ("brown", "brown"),
    ]
    color = models.CharField(max_length=7, choices=colors, default="white")
