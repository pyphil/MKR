# Generated by Django 4.0.5 on 2022-06-19 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mkr', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='kompetenzkarte',
            old_name='medien',
            new_name='medienkompetenz',
        ),
        migrations.AddField(
            model_name='kompetenzkarte',
            name='technik',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]