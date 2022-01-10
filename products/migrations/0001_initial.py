# Generated by Django 4.0.1 on 2022-01-10 04:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('email', models.CharField(max_length=300)),
                ('age', models.IntegerField()),
            ],
            options={
                'db_table': 'owners',
            },
        ),
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('age', models.IntegerField()),
                ('owner_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.owner')),
            ],
            options={
                'db_table': 'dogs',
            },
        ),
    ]
