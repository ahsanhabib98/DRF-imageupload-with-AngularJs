# Generated by Django 2.0.5 on 2019-02-19 16:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('image_upload', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='uploadimage',
            old_name='photo',
            new_name='image',
        ),
    ]
