# Generated by Django 4.0.5 on 2022-07-08 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_allowedemail_school'),
    ]

    operations = [
        migrations.RenameField(
            model_name='allowedemail',
            old_name='allowed_emails',
            new_name='emails',
        ),
    ]