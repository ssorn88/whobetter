from django.db import models


# Create your models here.

class Notice(models.Model):
    notice = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now=True)
