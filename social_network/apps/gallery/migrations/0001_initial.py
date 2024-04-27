# Generated by Django 5.0.1 on 2024-02-15 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GalleryImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='gallery/', verbose_name='Фотографии')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
            ],
        ),
    ]
