# Generated by Django 4.0.3 on 2022-03-21 23:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('init_finalapi', '0009_remove_employee_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='is_manager',
        ),
    ]
