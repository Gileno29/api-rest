# Generated by Django 4.1.5 on 2023-02-21 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0003_alter_item_estoque'),
    ]

    operations = [
        migrations.AddField(
            model_name='estoque',
            name='minimum',
            field=models.BigIntegerField(default=5),
        ),
    ]