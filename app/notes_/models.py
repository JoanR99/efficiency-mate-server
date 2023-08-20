from django.db import models
from django.contrib.auth.models import User


# class Colors(models.TextChoices):
#     WHITE = "white", _("white")
#     RED = "red", _("red")
#     YELLOW = "yellow", _("yellow")
#     ORANGE = "orange", _("orange")
#     BLUE = "blue", _("blue")
#     TEAL = "teal", _("teal")
#     GREEN = "green", _("green")
#     PURPLE = "purple", _("purple")
#     PINK = "pink", _("pink")
#     GRAY = "gray", _("gray")
#     BROWN = "brown", _("brown")


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
