from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType

# Create your models here.
class EmailId(models.Model):
    name = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = []

class Question(models.Model):
    email_ids = models.ManyToManyField(EmailId)
    subject = models.TextField(null=False, blank=False)
    content = models.TextField(null=False, blank=False)
    
