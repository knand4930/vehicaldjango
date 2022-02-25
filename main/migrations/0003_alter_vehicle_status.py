# Generated by Django 4.0.2 on 2022-02-25 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_rentvehicle_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='status',
            field=models.CharField(choices=[('available', 'available'), ('booked', 'booked'), ('unavailable', 'unavailable')], max_length=200),
        ),
    ]
