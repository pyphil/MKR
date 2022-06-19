from django.shortcuts import render
from .forms import KompetenzkarteForm


def home(request):
    return render(request, 'mkr.html', {})

def karte(request):
    f = KompetenzkarteForm()
    return render(request, 'karte.html', {'form': f})
