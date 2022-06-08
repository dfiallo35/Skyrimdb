from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey


class TypeOfDamage(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class DateAndTime(models.Model):
    date_time = models.DateTimeField()

    def __str__(self):
        return self.date_time

class Atack(models.Model):
    type_of_damage = models.ForeignKey(TypeOfDamage, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    avg_damage = models.IntegerField()

    def __str__(self):
        return self.name


class Spell(Atack):
    pass


class Character(models.Model):
    name = models.CharField(max_length=100)
    life_points = models.PositiveIntegerField()
    breed = models.CharField(max_length=100)
    weakness = models.ForeignKey(TypeOfDamage, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Player(Character):
    knows = models.ManyToManyField(Spell, through='InUse')

class Beast(Character):
    atack = models.ManyToManyField(Atack)

#TODO: in use field between Player and Spell
class InUse(models.Model):
    player = models.ForeignKey(Player, on_delete=models.DO_NOTHING, related_name='+')
    spell = models.ForeignKey(Spell, on_delete=models.DO_NOTHING, related_name='+')

class Battle(models.Model):
    character = models.ForeignKey(Character, on_delete=models.DO_NOTHING)
    date_and_time = models.ForeignKey(DateAndTime, related_name='+', on_delete=models.DO_NOTHING)
    # item = GenericForeignKey('date_and_time', 'character')
    battle_winner = models.OneToOneField(Character, on_delete=models.DO_NOTHING, related_name='+')


class Event(models.Model):
    battle = models.ForeignKey(Battle, on_delete=models.DO_NOTHING, related_name='+')
    character_atack = models.ForeignKey(Character, on_delete=models.DO_NOTHING, related_name='+')
    character_receive_atack = models.ForeignKey(Character, on_delete=models.DO_NOTHING, related_name='+')
    date_and_time = models.ForeignKey(DateAndTime, on_delete=models.DO_NOTHING, related_name='+')
    #TODO: attributes
    damage_taken = 100



