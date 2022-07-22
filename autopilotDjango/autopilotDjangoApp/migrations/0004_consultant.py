# Generated by Django 4.0.4 on 2022-06-14 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autopilotDjangoApp', '0003_alter_timesheet_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consultant',
            fields=[
                ('idConsultant', models.BigAutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'consultant',
                'managed': False,
            },
        ),
    ]
