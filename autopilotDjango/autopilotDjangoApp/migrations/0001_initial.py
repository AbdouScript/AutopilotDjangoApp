# Generated by Django 4.0.4 on 2022-05-27 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TimeSheet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('annee', models.SmallIntegerField()),
                ('Semaine', models.SmallIntegerField()),
                ('tempsPasse', models.FloatField()),
            ],
        ),
    ]