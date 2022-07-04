from django.shortcuts import render, redirect
from .forms import KompetenzkarteForm
from .models import Kompetenzkarte
from django.http import HttpResponse, FileResponse
from django.conf import settings
from django.contrib.auth.decorators import login_required


def home(request):
    mkr_objects = Kompetenzkarte.objects.all()
    return render(request, 'mkr.html', {'mkr_objects': mkr_objects})


@login_required
def karte(request):
    if request.method == 'GET':
        f = KompetenzkarteForm()
        return render(request, 'karte.html', {'form': f})
    if request.method == 'POST':
        f = KompetenzkarteForm(request.POST, request.FILES)
        if f.is_valid():
            f.save()
            return redirect('home')


@login_required
def download(request, filename):
    return FileResponse(
        # open(settings.MEDIA_ROOT + '/downloads/git-cheat-sheet-education.pdf', 'rb'), 
        open(settings.MEDIA_ROOT + '/downloads/' + filename, 'rb'), 
        as_attachment=True, 
        filename=filename
    )
