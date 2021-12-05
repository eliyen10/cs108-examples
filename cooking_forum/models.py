from django.db import models

# Create your models here.



class Person(models.Model):
    ''''''
    name = models.TextField(blank=True)

    def __str__(self):

        return self.name

class User(models.Model):
    '''shows the users and a recipe that they've created'''
    recipes = models.TextField(blank=True) # text
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    # username = models.TextField(blank=True) # author
    # image_url = models.URLField(blank=True) 

    def __str__(self):
        
        return f"{self.recipes} - {self.person}"

class Image(models.Model):
    ''''''
    image_url = models.URLField(blank=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return self.image_url









