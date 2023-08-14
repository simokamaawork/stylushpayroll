# Generated by Django 4.2.1 on 2023-06-28 11:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0025_commission_templates_department_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commision_saraly',
            name='daily_work',
        ),
        migrations.RemoveField(
            model_name='commision_saraly',
            name='monthly_work',
        ),
        migrations.RemoveField(
            model_name='commision_saraly',
            name='single_work',
        ),
        migrations.AddField(
            model_name='commision_saraly',
            name='department',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='first.department'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='commision_saraly',
            name='job_type',
            field=models.CharField(default='it', max_length=255),
            preserve_default=False,
        ),
    ]
