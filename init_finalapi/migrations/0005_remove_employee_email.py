# Generated by Django 4.0.3 on 2022-03-15 02:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('init_finalapi', '0004_employee_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='email',
        ),
    ]