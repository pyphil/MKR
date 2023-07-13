from django.shortcuts import render, redirect
from .forms import KompetenzkarteForm
from .models import Kompetenzkarte
from django.http import FileResponse
from django.conf import settings
from django.contrib.auth.decorators import login_required


def home(request):
    mkr_objects = Kompetenzkarte.objects.all()
    if request.GET.get('cookiebutton'):
        response = redirect('home')
        response.set_cookie('cookiebanner', False)
        return response
    try:
        cookiebanner = request.COOKIES['cookiebanner']
    except Exception:
        cookiebanner = True
    return render(request, 'mkr.html', {'mkr_objects': mkr_objects, 'cookiebanner': cookiebanner})


@login_required
def karte(request):
    if request.method == 'GET':
        f = KompetenzkarteForm(label_suffix="")
        return render(request, 'karte.html', {'form': f})
    if request.method == 'POST':
        f = KompetenzkarteForm(request.POST, request.FILES)
        if f.is_valid():
            f.save()
            return redirect('home')


@login_required
def karte_bearbeiten(request, id):
    obj = Kompetenzkarte.objects.get(id=id)
    if request.method == 'GET':
        f = KompetenzkarteForm(instance=obj, label_suffix="")
        return render(request, 'karte.html', {'form': f, 'edit': True})
    if request.method == 'POST':
        f = KompetenzkarteForm(request.POST, request.FILES, instance=obj)
        if f.is_valid():
            f.save()
            return redirect('home')


@login_required
def download(request, filename):
    return FileResponse(
        open(settings.MEDIA_ROOT + '/downloads/' + filename, 'rb'),
        as_attachment=True,
        filename=filename
    )


def rate_limit_exceeded_view(request):
    return render(request, 'rate_limit_exceeded.html')
