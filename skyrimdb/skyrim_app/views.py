from django.shortcuts import render
from django.db.models import Sum
from . import models as m


def fetch_battles():
    for b in m.Battle.objects.all():
        d = {
            # Stores data from usual Battle entity and extra
            # *start* gives the star date
            # *winner* gives the access to the winner info
            # *n_events* gives the number of events in a Battle
            # *total_d* gives the total damage of events in a battle
            # *participants* gives a string with the names of participants with comma between each one
            'start': b.start.strftime('%D %I:%M:%S %p'),
            'winner': b.winner.name,
            'n_events': b.events.count(),
            'total_d': b.events.aggregate(Sum('damage'))['damage__sum'],
            'participants': ', '.join((p['name'] for p in b.participants.values('name')))
        }
        yield d


def home(request):
    return render(request, 'pages/home.html')


def about(request):
    return render(request, 'pages/about.html')


def contact(request):
    return render(request, 'pages/contact.html')


def players(request):
    return render(request, 'pages/tables_pages/players.html')


def battles(request):
    return render(request,
                  'pages/tables_pages/battles.html',
                  {'battles': (b for b in fetch_battles())})


def beasts(request):
    return render(request, 'pages/tables_pages/beasts.html')


def spells(request):
    return render(request, 'pages/tables_pages/spells.html')
