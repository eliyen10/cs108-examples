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


class Recipe(models.Model):
    '''shows the users and a recipe that they've created'''
    ingredients = models.TextField(blank=True) # text
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    recipe_name = models.TextField(blank=True)
    

    def __str__(self):
        
        return f"{self.ingredients} - {self.person}"

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

