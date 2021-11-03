from django.db import models

# Create your models here.

class Quote(models.Model):
    '''represents a quote by a famous person'''

    text = models.TextField(blank=True)
    author = models.TextField(blank=True)
    image_url = models.URLField(blank=True)

    def __str__(self):
        '''Returns a string representation of the quote'''
        
        return f'"{self.text}" - {self.author}'
