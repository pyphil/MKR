from django.forms import ModelForm
from django import forms
from .models import Kompetenzkarte
from django.utils.safestring import mark_safe


class KompetenzkarteForm(ModelForm):
    class Meta:
        model = Kompetenzkarte
        fields = (
            'kategorie',
            'fach',
            'jgst',
            'vorhaben',
            'info',
            'medienkompetenz',
            'technik',
            'alle_teil',
            'pflicht_empf',
            'durchf_planung',
            'download',
        )
        labels = {
            'kategorie': mark_safe('<strong>Kategorie im Medienkompetenzrahmen</strong>'),
            'fach': mark_safe('<strong>Fach</strong>'),
            'jgst': mark_safe('<strong>Jahrgangsstufe</strong>'),
            'vorhaben': mark_safe('<strong>Unterrichtsvorhaben (Titel)</strong>'),
            'info': mark_safe('<strong>Detaillierte Informationen befinden sich hier (z.B. schulinternes Curriculum)</strong>'),
            'medienkompetenz': mark_safe('<strong>Medienkompetenz</strong>'),
            'technik': mark_safe('<strong>Technik</strong>'),
            'alle_teil': mark_safe('<strong>Das Vorhaben ist...</strong>'),
            'pflicht_empf': mark_safe('<strong>Das Vorhaben ist...</strong>'),
            'durchf_planung': mark_safe('<strong>Das Vorhaben ist...</strong>'),
            'download': mark_safe('<strong>Dateianhang für internen Bereich (Material, Konzept)</strong>')
        }
        widgets = {
            'kategorie': forms.Select(attrs={'class': 'form-select'}),
            'fach': forms.Select(attrs={'class': 'form-select'}),
            'jgst': forms.Select(attrs={'class': 'form-select'}),
            'vorhaben': forms.TextInput(attrs={'class': 'form-control'}),
            'info': forms.TextInput(attrs={'class': 'form-control'}),
            'medienkompetenz': forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}),
            'technik': forms.TextInput(attrs={'class': 'form-control'}),
            'alle_teil': forms.RadioSelect(),
            'pflicht_empf': forms.RadioSelect(),
            'durchf_planung': forms.RadioSelect(),
        }
