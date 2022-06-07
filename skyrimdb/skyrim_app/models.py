from django.db import models


class TypeOfDamage(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class DateAndTime(models.Model):
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return '%s %s' % (self.date, self.time)

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

    def __str__(self):
        return self.name

class Player(Character):
    knows = models.ManyToManyField(Spell, through='InUse')

class Beast(Character):
    atack = models.ManyToManyField(Atack)

#TODO: in use field between Player and Spell
class InUse(models.Model):
    spell_name = models.CharField(max_length=100)

class Battle(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    date_and_time = models.ForeignKey(DateAndTime, on_delete=models.CASCADE)
    battle_winner = models.ForeignKey(Character, on_delete=models.CASCADE)


class Event(models.Model):
    battle = models.ForeignKey(Battle, on_delete=models.CASCADE)
    character_atack = models.ForeignKey(Character, on_delete=models.CASCADE)
    character_receive_atack = models.ForeignKey(Character, on_delete=models.CASCADE)
    date_and_time = models.ForeignKey(DateAndTime, on_delete=models.CASCADE)
    #TODO: attributes
    damage_taken = 100



