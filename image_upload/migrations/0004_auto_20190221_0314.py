# Generated by Django 2.0.5 on 2019-02-20 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image_upload', '0003_auto_20190221_0243'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadimage',
            name='description',
            field=models.TextField(default='', verbose_name='Description of the uploaded image'),
        ),
        migrations.AddField(
            model_name='uploadimage',
            name='title',
            field=models.CharField(default='Unknown Picture', max_length=200, verbose_name='Title of the uploaded image'),
        ),
    ]
