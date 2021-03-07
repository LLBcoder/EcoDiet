from django.db import models
from django.contrib.auth.models import User

# Create your models here.
intolerances_choices = (
        ('None', 'None'),
        ('Dairy', 'Dairy'),
        ('Egg', 'Egg'),
        ('Gluten', 'Gluten'),
        ('Grain', 'Grain'),
        ('Peanut', 'Peanut'),
        ('Seafood', 'Seafood'),
        ('Sesame', 'Sesame'),
        ('Shellfish', 'Shellfish'),
        ('Soy', 'Soy'),
        ('Sulfite', 'Sulfite'),
        ('Tree Nut', 'Tree Nut'),
        ('Wheat', 'Wheat'),
	)

ingredients_choices = (
        ('None', 'None'),
        ('Tomato', 'tomato'),
        ('Mushrooms', 'mushrooms'),
        ('Olives', 'olives'),
)

diet_choices = (
        ('Regular', 'Regular'),
        ('Vegetarian', 'Vegetarian'),
        ('Pescetarian', 'Pescetarian'),
        ('Vegan', 'Vegan'),
)

diet_goal = (
        ('Vegetarian', 'Vegetarian'),
        ('Pescetarian', 'Pescetarian'),
        ('Vegan', 'Vegan'),
)

level_choices = (
        ('Trying it out!','Trying it out!'),
        ('Commited to change!', 'Commited to change!'),
        ('Full on transition!', 'Full on transition!')
)


class Intolerances(models.Model):
    intolerance = models.CharField(max_length=30, choices=intolerances_choices)

    def __str__(self):
        return self.intolerance

class Ingredients(models.Model):
    ingredient = models.CharField(max_length=30, choices=ingredients_choices)

    def __str__(self):
        return self.ingredient
        
class Restrictions(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    intolerance = models.ManyToManyField(Intolerances, blank=True)
    ingredient = models.ManyToManyField(Ingredients, blank=True)
    currentdiet = models.CharField(max_length=30, choices=diet_choices, default='Regular')
    dietgoal = models.CharField(max_length=30, choices=diet_goal, default='Vegetarian')
    level = models.CharField(max_length=30, choices=level_choices, default='Commited to change!')

    