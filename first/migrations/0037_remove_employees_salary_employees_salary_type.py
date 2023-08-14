# Generated by Django 4.2.1 on 2023-06-30 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0036_alter_dailywork_commision_rate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employees',
            name='salary',
        ),
        migrations.AddField(
            model_name='employees',
            name='salary_type',
            field=models.CharField(blank=True, choices=[('COMMISION', 'Commision'), ('FIXED', 'Fixed')], max_length=255),
        ),
    ]