# Generated by Django 4.1.5 on 2023-08-26 07:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mkr', '0010_kompetenzkarte_medienkenntnisse_lul_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='kompetenzkarte',
            name='changed',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='kompetenzkarte',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='kompetenzkarte',
            name='last_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='edited_datasets', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='kompetenzkarte',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
