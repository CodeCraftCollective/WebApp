# Generated by Django 4.2.7 on 2023-11-30 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_todolist_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]