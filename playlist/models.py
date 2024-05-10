from django.db import models

# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=55)
    embed = models.TextField()
    description = models.TextField(blank=True, null=True)
    likes = models.IntegerField(default=0)