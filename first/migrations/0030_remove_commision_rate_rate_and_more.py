# Generated by Django 4.2.1 on 2023-06-29 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0029_alter_dailywork_task'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commision_rate',
            name='rate',
        ),
        migrations.RemoveField(
            model_name='commission_templates',
            name='department',
        ),
        migrations.RemoveField(
            model_name='commission_templates',
            name='job_type',
        ),
        migrations.RemoveField(
            model_name='job_type',
            name='department',
        ),
        migrations.RemoveField(
            model_name='job_type',
            name='name',
        ),
        migrations.AlterField(
            model_name='job_type',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
