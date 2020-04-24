# Generated by Django 3.0.4 on 2020-04-19 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('personnel', models.IntegerField()),
                ('location', models.CharField(max_length=20)),
            ],
        ),
    ]