# Generated by Django 4.0.6 on 2022-08-12 19:53

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='move_count',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='game',
            name='game_uuid',
            field=models.UUIDField(default=uuid.UUID('ba1ddbc5-a75a-4b59-a3f4-26f3d606325b'), editable=False),
        ),
        migrations.AlterField(
            model_name='move',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('8bfd7601-2dda-4c5d-adee-6cebee7fa6da'), editable=False),
        ),
    ]
