from django.db import models
import random
from django.urls import reverse
# Create your models here.



class Person(models.Model):
    ''''''
    name = models.TextField(blank=True)

    def __str__(self):

        return self.name

    def get_random_recipe(self):
        '''displays a random recipe'''

        images = Image.objects.filter(person=self)

        return random.choice(images)

    # def get_all_quotes(self):
    #     '''Returns all quotes for this person'''

    #     return Quote.objects.filter(person = self)

    # def images(self):
    #     '''Returns all images  for this person'''

    #     return Image.objects.filter(person = self)

class User(models.Model):
    '''shows the users and a recipe that they've created'''
    recipes = models.TextField(blank=True) # text
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    # username = models.TextField(blank=True) # author
    # image_url = models.URLField(blank=True) 

    def __str__(self):
        
        return f"{self.recipes} - {self.person}"

    def get_absolute_url(self):
        '''provide a URL to show in this object'''

        return reverse('recipe', kwargs={'pk':self.pk})

class Image(models.Model):
    '''Represent an image, which is associated with a Person.'''

    image_url = models.URLField(blank=True) # url as a string
    person = models.ForeignKey('Person', on_delete=models.CASCADE)

    def __str__(self):
        '''Return a string representation of this image.'''

        return self.image_url

