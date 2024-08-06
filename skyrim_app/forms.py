from datetime import datetime
from typing import Any, Dict, Mapping, Optional
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

        if (attacker.pk,) not in battle.participants.values_list('pk'):
            errors['attacker'] = ValidationError(
                'The attacker in an event must be one of the participants of the battle it occurs')

        if (damaged.pk,) not in battle.participants.values_list('pk'):
            errors['damaged'] = ValidationError(
                'The damaged in an event must be one of the participants of the battle it occurs')

        try_beast = Beast.objects.filter(id=attacker.id)
        try_player = Player.objects.filter(id=attacker.id)

        if len(try_beast) > 0:
            attacker: Beast = try_beast[0]
            if (attack.pk,) not in attacker.attacks.values_list('pk'):
                errors['attack'] = ValidationError(
                    'The Beast attacking doesn\'t have the attack selected')
        else:
            attacker: Player = try_player[0]
            if (attack.pk,) not in attacker.spells_known.values_list('pk'):
                errors['attack'] = ValidationError(
                    'The Player attacking doesn\'t know the spell selected')

        if attack is not None and damaged is not None:
            avg = attack.average_dmg
            extra = 100 if damaged.weakness is not None and \
                damaged.weakness == attack.type else 0
            min = (avg*95+99)//100 + extra
            max = (avg*105)//100 + extra
            if (damage < min or damage > max):
                first_text = f'The damage should be between the 95%({min-extra}) and 105%' + \
                    f'({max-extra}) of the average damage of the attack'
                second_text = (f' (plus 100 extra for beeing the type of the attack({attack.type.name}) ' +
                               f'the weakness of the damaged)') if extra > 0 else ''
                errors['damage'] = ValidationError(first_text+second_text)
        if len(errors) > 0:
            raise ValidationError(errors)
        return cleaned_data
