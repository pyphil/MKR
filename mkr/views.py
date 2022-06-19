from django.shortcuts import render, redirect
from .forms import KompetenzkarteForm
from .models import Kompetenzkarte


def home(request):
    mkr_objects = Kompetenzkarte.objects.all()
    return render(request, 'mkr.html', {'mkr_objects': mkr_objects})


def karte(request):
    if request.method == 'GET':
        f = KompetenzkarteForm()
        return render(request, 'karte.html', {'form': f})
    if request.method == 'POST':
        f = KompetenzkarteForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect('home')
