from django.shortcuts import render
from django.db.models import Sum
from . import models as m


def fetch_battles():
    for b in m.Battle.objects.all():
        d = {
            # Stores data from usual Battle entity and extra
            # #= *start* gives the star date
            # #= *winner* gives the access to the winner info
            # #= *n_events* gives the number of events in a Battle
            # #= *total_d* gives the total damage of events in a battle
            # #= *participants* gives a string with the names of participants with comma between each one
            'start': b.start.strftime('%D %I:%M:%S %p'),
            'winner': b.winner.name,
            'n_events': b.events.count(),
            'total_d': b.events.aggregate(Sum('damage'))['damage__sum'],
            'participants': ', '.join((p['name'] for p in b.participants.values('name')))
        }
        yield d


def fetch_players():
    for p in m.Player.objects.all():
        d = {
            # Stores data from usual Player entity and extra
            # #= *name* gives the name of the player
            # #= *race* gives the name of the race
            # #= *hp* gives the current health points
            # #= *weakness* gives the damage type of the player weekness or
            # none if it doesn't have any
            # #= *spells* gives the list of knowed spells with the ones in use
            # marked and comma between them
            # #= *damage_in* gives the total damage recieved for the player in
            # all his battles
            # #= *damage_out* gives the total damage made by the player in all
            # his battles
            # #= *n_battles* gives the number of battles the player
            # #= *battles_won* gives the number of victories of the player
        }
        yield d


def fetch_beasts():
    for b in m.Beast.objects.all():
        d = {
            # Stores data from usual Beast entity and extra
            # #= *name* gives the name of the beast
            # #= *race* gives the name of the race
            # #= *hp* gives the current health points
            # #= *weakness* gives the damage type of the beast weekness or
            # none if it doesn't have any
            # #= *attacks* gives the list of knowed attacks comma between them
            # #= *damage_out* gives the total damage made by the beast in all
            # his battles
            # #= *n_battles* gives the number of battles the beast
            # #= *n_players* number of players faced by the beast
        }
        yield d


def fetch_spells():
    for s in m.Spell.objects.all():
        d = {
            # Stores data from usual Spell entity and extra
            # #= *name* gives the name of the spell
            # #= *avg_d* gives the average damage of the spell
            # #= *type* gives the name of the damage type it deals
            # #= *knows* gives the list of all players that knows the spell with
            # a comma between them
            # #= *uses* gives the list of all players that are using the spell with
            # a comma between them
            # #= *n_battles* gives the number of battles the spell has been used
        }
        yield d


def home(request):
    return render(request, 'pages/home.html')


def about(request):
    return render(request, 'pages/about.html')


def contact(request):
    return render(request, 'pages/contact.html')


def players(request):
    return render(request,
                  'pages/tables_pages/players.html',
                  {'players': (p for p in fetch_players())})


def battles(request):
    return render(request,
                  'pages/tables_pages/battles.html',
                  {'battles': (b for b in fetch_battles())})


def beasts(request):
    return render(request,
                  'pages/tables_pages/beasts.html',
                  {'beasts': (b for b in fetch_beasts())})


def spells(request):
    return render(request,
                  'pages/tables_pages/spells.html',
                  {'spells': (s for s in fetch_spells())})
