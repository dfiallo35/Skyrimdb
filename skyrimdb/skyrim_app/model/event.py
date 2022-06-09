from django.db import models
from .battle import *
from .character import *
from .dateandtime import *
from .attack import *

class Event(models.Model):
    battle = models.ForeignKey(Battle, on_delete=models.DO_NOTHING, related_name='+')
    character_atack = models.ForeignKey(Character, on_delete=models.DO_NOTHING, related_name='+')
    character_receive_atack = models.ForeignKey(Character, on_delete=models.DO_NOTHING, related_name='+')
    date_time = models.ForeignKey(DateAndTime, on_delete=models.DO_NOTHING, related_name='+')
    event_number = models.PositiveIntegerField()
    attack = models.ForeignKey(Attack, on_delete=models.DO_NOTHING, related_name='+')
    #TODO: calculate damage
    damage_taken = 100
    life_before_damage = 100