# Generated by Django 4.0.6 on 2022-08-06 14:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('game', '0006_alter_game_current_player_alter_game_game_uuid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='current_player',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='current_player', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='game',
            name='game_uuid',
            field=models.UUIDField(default=uuid.UUID('3481c7aa-8b28-465d-ae97-12ec1e3c38ec'), editable=False),
        ),
        migrations.AlterField(
            model_name='move',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('5150669e-5da0-4371-8b61-a45eb1f563f8'), editable=False),
        ),
    ]
