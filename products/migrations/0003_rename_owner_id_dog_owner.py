# Generated by Django 4.0.1 on 2022-01-10 08:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_dog_age'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dog',
            old_name='owner_id',
            new_name='owner',
        ),
    ]