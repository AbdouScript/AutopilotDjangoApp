# Generated by Django 4.0.4 on 2022-06-14 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autopilotDjangoApp', '0004_consultant'),
    ]

    operations = [
        migrations.CreateModel(
            name='Competence',
            fields=[
                ('idCompetence', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'ConsultantsCompetences',
                'managed': False,
            },
        ),
    ]