# Generated by Django 5.0.4 on 2024-05-12 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitems',
            name='is_completed',
            field=models.BooleanField(default=False),
        ),
    ]