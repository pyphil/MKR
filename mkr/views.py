from django.shortcuts import render, redirect
from .forms import KompetenzkarteForm
from .models import Kompetenzkarte, Fach
from django.http import FileResponse
from django.conf import settings
from django.contrib.auth.decorators import login_required


def home(request):
    try:
        cookiebanner = request.COOKIES['cookiebanner']
    except Exception:
        cookiebanner = True
    if request.GET.get('cookiebutton'):
        response = redirect('home')
        response.set_cookie('cookiebanner', False)
        return response

    mkr_objects = Kompetenzkarte.objects.all()

    if request.GET.get('fach_filter') and request.GET.get('fach_filter') != '0':
        mkr_objects = mkr_objects.filter(fach__fach=request.GET.get('fach_filter'))
        selected_fach = request.GET.get('fach_filter')
    else:
        selected_fach = None

    if request.GET.get('jgst_filter') and request.GET.get('jgst_filter') != '0':
        mkr_objects = mkr_objects.filter(jgst=request.GET.get('jgst_filter'))
        selected_jgst = request.GET.get('jgst_filter')
    else:
        selected_jgst = None

    # selected_jgst = None
    # if request.GET.get('fach_filter') and request.GET.get('fach_filter') != '0' and request.GET.get('jgst_filter') and request.GET.get('jgst_filter') != '0':
    #     selected_jgst = request.GET.get('jgst_filter')
    #     mkr_objects = Kompetenzkarte.objects.filter(
    #         fach=request.GET.get('fach_filter'), jgst=request.GET.get('jgst_filter')
    #     )
    # elif request.GET.get('fach_filter'):
    #     mkr_objects = Kompetenzkarte.objects.filter(fach=request.GET.get('fach_filter'))
    # elif request.GET.get('jgst_filter') and request.GET.get('jgst_filter') != '0':
    #     selected_jgst = request.GET.get('jgst_filter')
    #     mkr_objects = Kompetenzkarte.objects.filter(jgst=request.GET.get('jgst_filter'))
    # else:
    #     mkr_objects = Kompetenzkarte.objects.all()

    if request.GET.get('switch') == "on":
        switch = "off"
    else:
        switch = "on"

    return render(request, 'mkr.html', {
        'mkr_objects': mkr_objects,
        'cookiebanner': cookiebanner,
        'faecher': Fach.objects.all(),
        'selected_fach': selected_fach,
        'jgst_choices': Kompetenzkarte.JGST_CHOICES,
        'selected_jgst': selected_jgst,
        'switch': switch,
        }
    )


@login_required
def karte(request):
    if request.method == 'GET':
        f = KompetenzkarteForm(label_suffix="")
        return render(request, 'karte.html', {'form': f})
    if request.method == 'POST':
        f = KompetenzkarteForm(request.POST, request.FILES)
        if f.is_valid():
            karte = f.save(commit=False)
            karte.user = request.user
            karte.save()
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
            karte = f.save(commit=False)
            karte.last_user = request.user
            karte.save()
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
