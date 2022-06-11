from django.shortcuts import render

def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    return render(request, 'pages/contact.html')

def players(request):
    return render(request, 'pages/tables_pages/players.html')

def battles(request):
    return render(request, 'pages/tables_pages/battles.html')

def beasts(request):
    return render(request, 'pages/tables_pages/beasts.html')

def spells(request):
    return render(request, 'pages/tables_pages/spells.html')