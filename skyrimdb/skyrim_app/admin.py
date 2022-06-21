from typing import List, Tuple
from django.contrib import admin
from .models import *
from .forms import BattleForm, EventForm, PlayerForm
from .utils import *
from django.utils.html import format_html

admin.site.empty_value_display = '(None)'


class DamageTypeAdmin(admin.ModelAdmin):
    search_fields = ['name']


class RaceAdmin(admin.ModelAdmin):
    search_fields = ['name']


class AttackAdmin(admin.ModelAdmin):
    search_fields = ['name', 'type__name']
    list_display = ('__str__', 'type', 'average_dmg')
    list_filter = ('type',)


@admin.display(description='Spells',)
def player_spells(obj: Player):
    spells = get_spells(obj)

    return format_html('<br/>'.join(
        (name if not use else name+' [U]' for name, use in spells)
    ))


class PlayerModelAdmin(admin.ModelAdmin):
    form = PlayerForm
    filter_horizontal = ('spells_known',)
    search_fields = ['name', 'race__name']
    list_display = ('__str__', 'race', 'weakness', 'hp', player_spells)
    list_filter = ('race', 'weakness', 'spells_known')


@admin.display(description='Attacks',)
def beast_attacks(obj: Beast):
    attacks = get_attacks(obj)

    return format_html('<br/>'.join(attacks))


class BeastModelAdmin(admin.ModelAdmin):
    filter_horizontal = ('attacks',)
    search_fields = ['name', 'race__name']
    list_display = ('__str__', 'race', 'weakness', 'hp', beast_attacks)
    list_filter = ('race', 'weakness', 'attacks')


@admin.display(description='Participants',)
def battle_participants(obj: Battle):
    l = get_participants(obj)
    return format_html('<br/>'.join(l))


class BattleModelAdmin(admin.ModelAdmin):
    form = BattleForm
    date_hierarchy = 'start'
    filter_horizontal = ('participants',)
    search_fields = ['winner__name']
    list_display = ('__str__', 'start', 'winner', battle_participants)
    list_filter = ('winner', 'participants')


class EventModelAdmin(admin.ModelAdmin):
    form = EventForm
    date_hierarchy = 'time'
    search_fields = ['attacker__name', 'damaged__name', 'attack__name']
    list_display = ('__str__', 'time', 'attacker', 'damaged', 'attack')
    list_filter = ('attacker', 'damaged', 'attack')


admin.site.register(DamageType, DamageTypeAdmin)
admin.site.register(Race, RaceAdmin)

admin.site.register(Attack, AttackAdmin)
admin.site.register(Spell, AttackAdmin)

admin.site.register(Player, PlayerModelAdmin)
admin.site.register(Beast, BeastModelAdmin)

admin.site.register(Battle, BattleModelAdmin)
admin.site.register(Event, EventModelAdmin)
