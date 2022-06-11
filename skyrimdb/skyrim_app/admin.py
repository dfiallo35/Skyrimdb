from django.contrib import admin
from .models import *

# TODO: Fix Admin registration (if needed)
# class CharacterAd(admin.ModelAdmin):
#     list_display = ('name', 'life_points', 'breed', 'weakness',)
# class PlayerAd(admin.ModelAdmin):
#     list_display = ('name', 'life_points', 'breed', 'weakness')
# class BeastAd(admin.ModelAdmin):
#     list_display = ('name', 'life_points', 'breed', 'weakness')


# class AttackAd(admin.ModelAdmin):
#     list_display = ('name', 'type_of_damage', 'avg_damage',)
# class BeastAttackAd(admin.ModelAdmin):
#     list_display = ('name', 'type_of_damage', 'avg_damage',)
# class SpellAd(admin.ModelAdmin):
#     list_display = ('name', 'type_of_damage', 'avg_damage',)

# class PlayerKnowAd(admin.ModelAdmin):
#     list_display = ('player', 'spell')
# class BeastKnowAd(admin.ModelAdmin):
#     list_display = ('beast', 'attack')
# class InUseAd(admin.ModelAdmin):
#     list_display = ('player', 'spell')


# class BattleAd(admin.ModelAdmin):
#     list_display = ('date_time', 'battle_winner')

# class BattleParticipantAd(admin.ModelAdmin):
#     list_display = ('battle', 'character')

# class EventAd(admin.ModelAdmin):
#     list_display = ('battle', 'character_atack', 'character_receive_atack', 'date_time', 'damage_taken')

# class BreedAd(admin.ModelAdmin):
#     list_display = ('breed',)

# class TypeOfDamageAd(admin.ModelAdmin):
#     list_display = ('type_of_damage',)

# class DateAndTimeAd(admin.ModelAdmin):
#     list_display = ('date_time',)

admin.site.register(DamageType)
admin.site.register(Race)

admin.site.register(Attack)
admin.site.register(Spell)

admin.site.register(Player)
admin.site.register(Beast)

admin.site.register(Battle)
admin.site.register(Event)

# admin.site.register(Character, CharacterAd)
# admin.site.register(Player, PlayerAd)
# admin.site.register(Beast, BeastAd)

# admin.site.register(Attack, AttackAd)
# admin.site.register(Spell, SpellAd)
# admin.site.register(PlayerKnow, PlayerKnowAd)
# admin.site.register(InUse, InUseAd)
# admin.site.register(BeastAttack, BeastAttackAd)
# admin.site.register(BeastKnow, BeastKnowAd)


# admin.site.register(TypeOfDamage, TypeOfDamageAd)
# admin.site.register(DateAndTime, DateAndTimeAd)


# admin.site.register(Battle, BattleAd)
# admin.site.register(BattleParticipant, BattleParticipantAd)

# admin.site.register(Event, EventAd)

# admin.site.register(Breed, BreedAd)
