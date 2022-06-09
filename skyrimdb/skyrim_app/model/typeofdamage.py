from django.db import models

class TypeOfDamage(models.Model):
    #TODO: delete CHOICES
    CHOICES = [
        ('Fire', 'Fire'),
        ('Frost', 'Frost'),
        ('Poison', 'Poison'),
        ('Shock', 'Shock'),

    ]
    type_of_damage = models.CharField(max_length=100, choices=CHOICES)
    
    def __str__(self):
        return self.type_of_damage