# Generated by Django 5.0.1 on 2024-04-22 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_alter_galleryimage_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galleryimage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='gallery/', verbose_name='Фотографии'),
        ),
    ]