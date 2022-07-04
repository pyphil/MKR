# Generated by Django 4.0.5 on 2022-07-03 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mkr', '0004_alter_kompetenzkarte_kategorie'),
    ]

    operations = [
        migrations.AddField(
            model_name='kompetenzkarte',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='downloads/'),
        ),
        migrations.AlterField(
            model_name='kompetenzkarte',
            name='kategorie',
            field=models.CharField(choices=[('11', '1.1 Medienausstattung'), ('12', '1.2 Digitale Werkzeuge'), ('13', '1.3 Datenorganisation'), ('14', '1.4 Datenschutz und Informationssicherheit'), ('21', '2.1 Informationsrecherche'), ('22', '2.2 Informationsauswertung'), ('23', '2.3 Informationsbewertung'), ('24', '2.4 Informationskritik'), ('31', '3.1 Kommunikations- und Kooperationsprozesse'), ('32', '3.2 Kommunikations- und Kooperationsregeln'), ('33', '3.3 Kommunikation und Kooperation in der Gesellschaft'), ('34', '3.4 Cybergewalt und -kriminalität'), ('41', '4.1 Medienproduktion und Präsentation'), ('42', '4.2 Gestaltungsmittel'), ('43', '4.3 Quellendokumentation'), ('44', '4.4 Rechtliche Grundlagen'), ('51', '5.1 Medienanalyse'), ('52', '5.2 Meinungsbildung'), ('53', '5.3 Identitätsbildung'), ('54', '5.4 Selbstregulierte Mediennutzung'), ('61', '6.1 Prinzipien der digitalen Welt'), ('62', '6.2 Algorithmen erkennen'), ('63', '6.3 Modellieren und Programmieren'), ('64', '6.4 Bedeutung von Algorithmen')], max_length=2),
        ),
    ]