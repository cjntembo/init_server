# Generated by Django 4.0.3 on 2022-03-22 03:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('init_finalapi', '0012_picklist_pick_list_line'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='picklist',
            name='pick_list_line',
        ),
    ]
