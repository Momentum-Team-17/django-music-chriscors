# Generated by Django 4.1.7 on 2023-03-05 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0006_alter_album_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='artwork',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
