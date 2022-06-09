from django.db import models
from .character import *
from .typeofdamage import *

class Attack(models.Model):
    type_of_damage = models.ForeignKey(TypeOfDamage, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    avg_damage = models.IntegerField()

    def __str__(self):
        return self.name

class Spell(Attack):
    pass

class BeastAttack(Attack):
    pass

class PlayerKnow(models.Model):
    player = models.ForeignKey(Player, on_delete=models.DO_NOTHING, related_name='+')
    spell = models.ForeignKey(Spell, on_delete=models.DO_NOTHING, related_name='+')

    def __str__(self):
        return self.spell.name

class InUse(models.Model):
    #TODO: select in use spells from Knows
    player = models.ForeignKey(Player, on_delete=models.DO_NOTHING, related_name='+')
    # try:
    #     CHOICES = [ (a, a) for a in list(Spell.objects.all())]
    # except Know.DoesNotExist:
    #     CHOICES = []
    spell = models.ForeignKey(Spell, on_delete=models.DO_NOTHING, related_name='+')


class BeastKnow(models.Model):
    beast = models.ForeignKey(Beast, on_delete=models.DO_NOTHING, related_name='+')
    attack = models.ForeignKey(BeastAttack, on_delete=models.DO_NOTHING, related_name='+')