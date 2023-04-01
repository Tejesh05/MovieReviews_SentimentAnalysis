# models.py
from django.db import models

class Review(models.Model):
    Username = models.TextField()
    Email = models.EmailField()
    review_text = models.TextField()
    sentiment = models.CharField(max_length=10)

    def __str__(self):
        return self.review_text
