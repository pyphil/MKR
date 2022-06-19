from django.shortcuts import render, redirect
from .forms import KompetenzkarteForm


def home(request):
    return render(request, 'mkr.html', {})

def karte(request):
    if request.method == 'GET':
        f = KompetenzkarteForm()
        return render(request, 'karte.html', {'form': f})
    if request.method == 'POST':
        f = KompetenzkarteForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect('home')
