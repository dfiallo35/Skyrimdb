# from .atack import Spell, BeastAtack

# def get_spell(self):
#         try:
#             spell = list(Spell.objects.filter(id= self.id))
#             return "\n".join([x.name for x in spell])
#         except Spell.DoesNotExist:
#             return '---'

# def get_atack(self):
#         atack = list(BeastAtack.objects.filter(id= self.id))
#         return "\n".join([x.name for x in atack])