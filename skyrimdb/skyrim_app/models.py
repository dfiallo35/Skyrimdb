from django.db import models


class Race(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = ("Race")
        verbose_name_plural = ("Races")
        ordering = ["name"]

    def __str__(self):
        return self.name


class DamageType(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = ("Damage Type")
        verbose_name_plural = ("damage types")
        ordering = ["name"]

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
                                 related_query_name="%(class)ss_with_weakness",
                                 blank=True, null=True)
    hp = models.PositiveIntegerField("Current Hit Points")

    class Meta:
        verbose_name = ("Character")
        verbose_name_plural = ("Characters")
        ordering = ["name"]

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
        ordering = ["name"]

    def __str__(self):
        return self.name


class Spell(Attack):

    class Meta:
        verbose_name = ("Spell")
        verbose_name_plural = ("Spells")
        ordering = ["name"]

    def __str__(self):
        return self.name


class Player(Character):
    spells_known = models.ManyToManyField(Spell, verbose_name="Spells Known",
                                          related_name="%(class)ss",
                                          related_query_name="%(class)ss_with",
                                          blank=True)
    spell_slot1 = models.ForeignKey(Spell, on_delete=models.PROTECT,
                                    verbose_name="Spell in use in Slot 1",
                                    related_name="%(class)ss_1",
                                    related_query_name="%(class)ss_in_slot1",
                                    blank=True, null=True)
    spell_slot2 = models.ForeignKey(Spell, on_delete=models.PROTECT,
                                    verbose_name="Spell in use in Slot 2",
                                    related_name="%(class)ss_2",
                                    related_query_name="%(class)ss_in_slot2",
                                    blank=True, null=True)
    spell_slot3 = models.ForeignKey(Spell, on_delete=models.PROTECT,
                                    verbose_name="Spell in use in Slot 3",
                                    related_name="%(class)ss_3",
                                    related_query_name="%(class)ss_in_slot3",
                                    blank=True, null=True)

    class Meta:
        verbose_name = ("Player")
        verbose_name_plural = ("Players")
        ordering = ["name"]

    def __str__(self):
        return self.name


class Beast(Character):
    attacks = models.ManyToManyField(Attack, verbose_name="Attacks",
                                     related_name="%(class)ss",
                                     related_query_name="%(class)ss_with",
                                     blank=True)

    class Meta:
        verbose_name = ("Beast")
        verbose_name_plural = ("Beasts")
        ordering = ["name"]

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

    def __str__(self):
        duration = (self.start if self.events.count() ==
                    0 else self.events.latest().time)-self.start
        return ''.join([
            f"{str(self.start)} - battle with winner ",
            f"{self.winner.name} and duration {str(duration)}"
        ])

    class Meta:
        verbose_name = ("Battle")
        verbose_name_plural = ("Battles")
        get_latest_by = "start"
        ordering = ["-start"]


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
    attack = models.ForeignKey(Attack, on_delete=models.PROTECT,
                               verbose_name="Attack",
                               related_name="%(class)ss",
                               related_query_name="%(class)ss_with")
    damage = models.PositiveIntegerField(verbose_name="Damage Inflicted")

    def __str__(self):
        return f"At {str(self.time)} " +\
            f"{self.attacker.name} used {self.attack.name} on {self.damaged.name}"

    class Meta:
        verbose_name = ("Event")
        verbose_name_plural = ("Events")
        get_latest_by = "time"
        ordering = ["time"]
