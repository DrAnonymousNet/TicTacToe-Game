# Generated by Django 4.0.6 on 2022-08-06 14:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('game', '0005_game_current_player_alter_game_game_uuid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='current_player',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='current_player', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='game',
            name='game_uuid',
            field=models.UUIDField(default=uuid.UUID('a2aac6cb-baac-4d89-85dc-f372dec3645f'), editable=False),
        ),
        migrations.AlterField(
            model_name='move',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('27f6344c-8aa4-4f4f-9489-f31b02315c2d'), editable=False),
        ),
    ]
