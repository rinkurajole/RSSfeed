"""
Used for defining model for RSS feed.
"""
from django.db import models


class Feed(models.Model):
    """
    defining fields for feed data.
    """
    title = models.TextField(null=True)
    description = models.TextField(null=True)
    publishdate = models.DateTimeField()
    guid = models.TextField(unique=True)
    url = models.TextField()
    srcurl = models.TextField()
