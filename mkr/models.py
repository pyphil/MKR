from django.db import models


class Fach(models.Model):
    fach = models.CharField(max_length=50)

    def __str__(self):
        return self.fach

    class Meta:
        verbose_name_plural = 'Fächer'


class Kompetenzkarte(models.Model):
    kategorie = models.CharField(max_length=50)
    fach = models.ForeignKey(Fach, on_delete=models.DO_NOTHING)
    JGST_CHOICES = [
        ('05', 'Jgst. 5'),
        ('06', 'Jgst. 6'),
        ('07', 'Jgst. 7'),
        ('08', 'Jgst. 8'),
        ('09', 'Jgst. 9'),
        ('10', 'Jgst. 10'),
        ('11', 'Jgst. EF'),
        ('12', 'Jgst. Q1'),
        ('13', 'Jgst. Q2'),
    ]
    jgst = models.CharField(max_length=2, choices=JGST_CHOICES)
    vorhaben = models.CharField(max_length=200)
    info = models.CharField(max_length=200)
    medienkompetenz = models.CharField(max_length=200)
    technik = models.CharField(max_length=200)
    ALLE_TEIL_CHOICES = [
        ('0', 'ist für alle '),
        ('1', 'Teilgruppe'),
    ]
    alle_teil = models.CharField(max_length=1, choices=ALLE_TEIL_CHOICES)
    PFLICHT_EMPF_CHOICES = [
        ('0', 'Pflicht'),
        ('1', 'Empfehlung'),
    ]
    pflicht_empf = models.CharField(max_length=1, choices=PFLICHT_EMPF_CHOICES)
    DURCHF_PLANUNG_CHOICES = [
        ('0', 'wird durchgeführt'),
        ('1', 'Planung/Umsetzung'),
    ]
    durchf_planung = models.CharField(max_length=1, choices=DURCHF_PLANUNG_CHOICES)

    class Meta:
        verbose_name_plural = 'Kompetenzkarten'
