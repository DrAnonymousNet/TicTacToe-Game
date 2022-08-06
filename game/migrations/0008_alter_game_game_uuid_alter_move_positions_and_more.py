# Generated by Django 4.0.6 on 2022-08-06 14:47

import django.contrib.postgres.fields
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0007_alter_game_current_player_alter_game_game_uuid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='game_uuid',
            field=models.UUIDField(default=uuid.UUID('4f20a995-5a1a-4527-88ee-fcdb389a3088'), editable=False),
        ),
        migrations.AlterField(
            model_name='move',
            name='positions',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=5), blank=True, size=None),
        ),
        migrations.AlterField(
            model_name='move',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('f4a51766-d9a1-447a-ac69-2260f26d6455'), editable=False),
        ),
    ]
