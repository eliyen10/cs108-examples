from django.db import models

class Person(models.Model):
    '''Encapsulate the concept of a person, who said some famous quote.'''

    name = models.TextField(blank=False)
    
    def __str__(self):
        '''Return a string representaton of this Person.'''
        return self.name
      
class Quote(models.Model):
    '''Encapsulate the idea of a quote (i.e., text).'''

    # data attributes of a quote:
    text = models.TextField(blank=True)
    person = models.ForeignKey('Person', on_delete=models.CASCADE) ## TEMPORARILY COMMENTED OUT

    def __str__(self):
        '''Return a string representation of this Quote object.'''
        return f'"{self.text}" - {self.person}'

class Image(models.Model):
    '''Represent an image, which is associated with a Person.'''

    image_url = models.URLField(blank=True) # url as a string
    person = models.ForeignKey('Person', on_delete=models.CASCADE)

    def __str__(self):
        '''Return a string representation of this image.'''

        return self.image_url