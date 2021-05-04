# Generated by Django 3.0.6 on 2020-06-20 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PredResults',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Patient_ID', models.FloatField()),
                ('Patient_Age', models.FloatField()),
                ('Patient_Gender', models.FloatField()),
                ('Patient_Blood_Pressure', models.FloatField()),
                ('Patient_Heartrate', models.FloatField()),
                ('Heart_Disease', models.CharField(max_length=30)),
            ],
        ),
    ]
