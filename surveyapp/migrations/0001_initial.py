# Generated by Django 2.1 on 2020-03-22 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.CharField(max_length=300)),
                ('name', models.CharField(max_length=20)),
                ('phone_number', models.CharField(max_length=12)),
            ],
        ),
    ]
