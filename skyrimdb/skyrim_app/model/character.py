from django.db import models
from .breed import *
from .typeofdamage import *

class Character(models.Model):
    name = models.CharField(max_length=100)
    life_points = models.PositiveIntegerField()
    breed = models.ForeignKey(Breed, on_delete=models.DO_NOTHING)
    weakness = models.ForeignKey(TypeOfDamage, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Player(Character):
    pass

class Beast(Character):
    pass