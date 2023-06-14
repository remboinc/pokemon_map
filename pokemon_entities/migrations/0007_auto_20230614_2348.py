# Generated by Django 3.1.14 on 2023-06-14 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0006_pokemonentity_pokemon'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemonentity',
            name='appeared_at',
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name='pokemonentity',
            name='disappeared_at',
            field=models.DateTimeField(default=None),
        ),
    ]
