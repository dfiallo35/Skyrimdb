from typing import Iterable, List, Tuple
from . import models as m


def get_attacks(beast: m.Beast) -> Iterable[str]:
    return (a['name'] for a in beast.attacks.values('name'))


def get_spells(player: m.Player) -> Iterable[Tuple[str, bool]]:
    def gen():
        for spell in player.spells_known.all().values('pk', 'name'):
            text: str = spell['name']
            use = False
            if player.spell_slot1 is not None:
                if spell['pk'] == player.spell_slot1.pk:
                    use = True
            if player.spell_slot2 is not None:
                if spell['pk'] == player.spell_slot2.pk:
                    use = True
            if player.spell_slot3 is not None:
                if spell['pk'] == player.spell_slot3.pk:
                    use = True
            yield (text, use)

    return (v for v in gen())


def get_participants(battle: m.Battle) -> Iterable[str]:
    return (p['name'] for p in battle.participants.all().values('name'))
