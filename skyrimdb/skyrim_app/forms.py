from datetime import datetime
from typing import Dict
from django.forms import ModelForm, ValidationError
from .models import *


class PlayerForm(ModelForm):
    class Meta:
        model = Player
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        errors: Dict[str, ValidationError] = {}
        for i in range(3):
            field = f'spell_slot{i+1}'
            if field in cleaned_data.keys() and\
                    cleaned_data[field] not in cleaned_data['spells_known'] and\
                    cleaned_data[field] is not None:
                errors[field] = ValidationError(
                    f"To mark a spell as equipped it must stored as knowed spell")
        if len(errors) > 0:
            raise ValidationError(errors)
        return cleaned_data


class BattleForm(ModelForm):
    class Meta:
        model = Battle
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        errors: Dict[str, ValidationError] = {}
        if cleaned_data['winner'] not in cleaned_data['participants']:
            errors['winner'] = ValidationError(
                f"The winner must be one of the participants of the battle")
        if len(errors) > 0:
            raise ValidationError(errors)
        return cleaned_data


class EventForm(ModelForm):

    class Meta:
        model = Battle
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        errors: Dict[str, ValidationError] = {}
        battle: Battle = cleaned_data['battle']
        attack: Attack = cleaned_data['attack']
        attacker: Character = cleaned_data['attacker']
        damaged: Character = cleaned_data['damaged']
        damage: int = cleaned_data['damage']
        time: datetime = cleaned_data['time']

        if time < battle.start:
            errors['time'] = ValidationError(
                'One event on a battle can\'t occur before the battle start')

        if attacker not in battle.participants.all():
            errors['attacker'] = ValidationError(
                'The attacker in an event must be one of the participants of the battle it occurs')

        if damaged not in battle.participants.all():
            errors['damaged'] = ValidationError(
                'The damaged in an event must be one of the participants of the battle it occurs')

        try_beast = Beast.objects.filter(id=attacker.id)
        try_player = Player.objects.filter(id=attacker.id)

        if len(try_beast) > 0:
            attacker: Beast = try_beast[0]
            if attack not in attacker.attacks.all():
                errors['attack'] = ValidationError(
                    'The Beast attacking doesn\'t know the attack selected')
        else:
            attacker: Player = try_player[0]
            if attack not in attacker.spells_known.all():
                errors['attack'] = ValidationError(
                    'The Player attacking doesn\'t know the spell selected')

        # TODO: Validate damage done

        return cleaned_data

# TODO: Rest of validation
