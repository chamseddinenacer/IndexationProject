# models.py
from django.db import models

class Document(models.Model):
    contenu = models.TextField()

    def __str__(self):
        return f"Document {self.id}"
