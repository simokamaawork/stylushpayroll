# Generated by Django 4.2.1 on 2023-06-30 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0038_employees_date_first_employees'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advancesalary',
            name='month',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='advancesalary',
            name='reason',
            field=models.TextField(blank=True),
        ),
    ]
