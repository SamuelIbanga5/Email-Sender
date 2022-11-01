from django.db import models
from ckeditor.fields import RichTextField

class Message(models.Model):
    message = RichTextField(blank=False)