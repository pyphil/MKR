from django.forms import ModelForm
from django import forms
from .models import Kompetenzkarte


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
        )
        labels = {
            'kategorie': 'Kategorie im Medienkompetenzrahmen:',
            'fach': 'Fach:',
            'jgst': 'Jahrgangsstufe:',
            'vorhaben': 'Unterrichtsvorhaben (Titel):',
            'info': 'Detaillierte Informationen befinden sich hier (z.B. schulinternes Curriculum):',
            'medienkompetenz': 'Medienkompetenz:',
            'technik': 'Technik:',
            'alle_teil': 'Das Vorhaben ist...',
            'pflicht_empf': 'Das Vorhaben ist...',
            'durchf_planung': 'Das Vorhaben ist...',
        }
        widgets = {
            'kategorie': forms.Select(attrs={'class': 'form-select'}),
            'fach': forms.Select(attrs={'class': 'form-select'}),
            'jgst': forms.Select(attrs={'class': 'form-select'}),
            'vorhaben': forms.TextInput(attrs={'class': 'form-control'}),
            'info': forms.TextInput(attrs={'class': 'form-control'}),
            'medienkompetenz': forms.Textarea(attrs={'class': 'form-control'}),
            'technik': forms.TextInput(attrs={'class': 'form-control'}),
            'alle_teil': forms.RadioSelect(),
            'pflicht_empf': forms.RadioSelect(),
            'durchf_planung': forms.RadioSelect(),
        }
