# Generated by Django 3.2.15 on 2022-11-11 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applibros', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='libros',
            name='img',
            field=models.ImageField(default='img', upload_to='gallery'),
            preserve_default=False,
        ),
    ]
