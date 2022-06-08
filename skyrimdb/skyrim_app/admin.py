from django.contrib import admin
from .models import *

class CharacterAd(admin.ModelAdmin):
    list_display = ('name', 'life_points', 'breed', 'weakness',)

class TypeOfDamageAd(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Character, CharacterAd)
admin.site.register(TypeOfDamage, TypeOfDamageAd)