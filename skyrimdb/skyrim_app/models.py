# from .model.attack import *
# from .model.battle import *
# from .model.breed import *
# from .model.character import *
# from .model.dateandtime import *
# from .model.event import *
# from .model.typeofdamage import *
# NOTE: This comments are the old models

from django.db import models


class Race(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = ("Race")
        verbose_name_plural = ("Races")

    def __str__(self):
        return self.name


class DamageType(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = ("Damage Type")
        verbose_name_plural = ("damage types")

    def __str__(self):
        return self.name


class Character(models.Model):
    name = models.CharField(max_length=50, unique=True)
    race = models.ForeignKey(Race, verbose_name="Race",
                             on_delete=models.PROTECT,
                             related_name="%(class)ss",
                             related_query_name="%(class)ss_with")
    weakness = models.ForeignKey(DamageType, verbose_name="Weakness",
                                 on_delete=models.PROTECT,
                                 related_name="%(class)ss",
                                 related_query_name="%(class)ss_with_weakness")
    hp = models.PositiveIntegerField("Current Hit Points")

    class Meta:
        verbose_name = ("Character")
        verbose_name_plural = ("Characters")

    def __str__(self):
        return self.name


class Attack(models.Model):
    name = models.CharField(max_length=50, unique=True)
    type = models.ForeignKey(DamageType, verbose_name="Type",
                             on_delete=models.PROTECT,
                             related_name="%(class)ss",
                             related_query_name="%(class)ss_with")
    average_dmg = models.PositiveIntegerField("Average Damage")

    class Meta:
        verbose_name = ("Attack")
        verbose_name_plural = ("Attacks")

    def __str__(self):
        return self.name


class Spell(Attack):

    class Meta:
        verbose_name = ("Spell")
        verbose_name_plural = ("Spells")

    def __str__(self):
        return self.name


class Player(Character):
    spells_known = models.ManyToManyField(Spell, verbose_name="Spells Known",
                                          related_name="%(class)ss",
                                          related_query_name="%(class)ss_with")
    spell_slot1 = models.ForeignKey(Spell, on_delete=models.PROTECT,
                                    verbose_name="Spell in use in Slot 1",
                                    related_name="%(class)ss_1",
                                    related_query_name="%(class)ss_in_slot1")
    spell_slot2 = models.ForeignKey(Spell, on_delete=models.PROTECT,
                                    verbose_name="Spell in use in Slot 2",
                                    related_name="%(class)ss_2",
                                    related_query_name="%(class)ss_in_slot2")
    spell_slot3 = models.ForeignKey(Spell, on_delete=models.PROTECT,
                                    verbose_name="Spell in use in Slot 3",
                                    related_name="%(class)ss_3",
                                    related_query_name="%(class)ss_in_slot3")

    class Meta:
        verbose_name = ("Player")
        verbose_name_plural = ("Players")

    def __str__(self):
        return self.name


class Beast(Character):
    attacks = models.ManyToManyField(Attack, verbose_name="Attacks",
                                     related_name="%(class)ss",
                                     related_query_name="%(class)ss_with")

    class Meta:
        verbose_name = ("Beast")
        verbose_name_plural = ("Beasts")

    def __str__(self):
        return self.name


class Battle(models.Model):
    start: models.DateTimeField = models.DateTimeField(
        verbose_name="Start time")
    participants = models.ManyToManyField(Character, verbose_name="Battle Participants",
                                          related_name="%(class)ss",
                                          related_query_name="%(class)ss_in")
    winner = models.ForeignKey(Character, on_delete=models.PROTECT,
                               verbose_name="Winner",
                               related_name="%(class)ss_win",
                               related_query_name="%(class)ss_won")

    class Meta:
        verbose_name = ("Battle")
        verbose_name_plural = ("Battles")


class Event(models.Model):
    battle = models.ForeignKey(Battle, on_delete=models.CASCADE,
                               related_name="%(class)ss",
                               related_query_name="%(class)ss_in")
    time = models.DateTimeField(verbose_name="Time of the Event")
    attacker = models.ForeignKey(Character, on_delete=models.PROTECT,
                                 verbose_name="Attacker",
                                 related_name="%(class)ss_attack",
                                 related_query_name="%(class)ss_in_attack")
    damaged = models.ForeignKey(Character, on_delete=models.PROTECT,
                                verbose_name="Damaged in Event",
                                related_name="%(class)ss_damage",
                                related_query_name="%(class)s")
    damage = models.PositiveIntegerField(verbose_name="Damage Inflicted")

    class Meta:
        verbose_name = ("Event")
        verbose_name_plural = ("Events")
