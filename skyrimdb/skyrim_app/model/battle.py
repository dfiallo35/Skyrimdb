from django.db import models
from .character import *
from .dateandtime import *

class Battle(models.Model):
    date_time = models.ForeignKey(DateAndTime, related_name='+', on_delete=models.DO_NOTHING)
    battle_winner = models.ForeignKey(Character, on_delete=models.DO_NOTHING, related_name='+')

class BattleParticipant(models.Model):
    character = models.ForeignKey(Character, on_delete=models.DO_NOTHING)
    battle = models.ForeignKey(Battle, on_delete=models.DO_NOTHING, related_name='+')
