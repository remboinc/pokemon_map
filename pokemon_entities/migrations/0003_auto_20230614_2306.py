# Generated by Django 3.1.14 on 2023-06-14 23:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0002_auto_20230614_2303'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Pokemons',
            new_name='Pokemon',
        ),
    ]
