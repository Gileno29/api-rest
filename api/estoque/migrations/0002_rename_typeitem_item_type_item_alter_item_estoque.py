# Generated by Django 4.1.5 on 2023-02-06 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='typeItem',
            new_name='type_item',
        ),
        migrations.AlterField(
            model_name='item',
            name='estoque',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='estoque.estoque'),
        ),
    ]