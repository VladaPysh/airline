# Generated by Django 3.1.4 on 2021-02-13 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0002_auto_20210212_1429'),
    ]

    operations = [
        migrations.AddField(
            model_name='people',
            name='flights',
            field=models.ManyToManyField(blank=True, related_name='people', to='flights.Flight'),
        ),
    ]
