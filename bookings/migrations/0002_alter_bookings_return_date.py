# Generated by Django 4.0.1 on 2022-01-29 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookings',
            name='return_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
