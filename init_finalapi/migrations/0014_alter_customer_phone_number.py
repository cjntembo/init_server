# Generated by Django 4.0.3 on 2022-03-22 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('init_finalapi', '0013_remove_picklist_pick_list_line'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone_number',
            field=models.CharField(max_length=50, null=True),
        ),
    ]