# Generated by Django 4.0.6 on 2023-08-09 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0070_alter_dailywork_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailywork',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
