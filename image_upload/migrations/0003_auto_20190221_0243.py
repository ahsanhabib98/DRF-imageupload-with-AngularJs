# Generated by Django 2.0.5 on 2019-02-20 20:43

from django.db import migrations, models
import image_upload.models


class Migration(migrations.Migration):

    dependencies = [
        ('image_upload', '0002_auto_20190219_2222'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadimage',
            name='thumbnail',
            field=models.ImageField(blank=True, upload_to='', verbose_name='Thumbnail of the uploaded image'),
        ),
        migrations.AlterField(
            model_name='uploadimage',
            name='image',
            field=models.ImageField(upload_to=image_upload.models.scramble_uploaded_filename, verbose_name='Uploaded image'),
        ),
    ]