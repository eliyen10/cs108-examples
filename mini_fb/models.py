from django.db import models

# Create your models here.

class Profile(models.Model):
    '''How the fb page is gonna get set up'''
    first_name = models.TextField(blank=True)
    last_name = models.TextField(blank=True)
    city = models.TextField(blank=True)
    email_address = models.TextField(blank=True)
    profile_img_url = models.TextField(blank=True)


    def __str__(self):
        '''Returns a string representation of the quote'''

        return f'{self.first_name} - {self.last_name}'