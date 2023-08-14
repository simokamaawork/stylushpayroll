# Generated by Django 4.2.1 on 2023-07-06 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0041_rename_task_dailywork_job_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailywork',
            name='job_type',
            field=models.ForeignKey(choices=[('CHOICE A', '25'), ('CHOICE B', '30'), ('CHOICE C', '35'), ('CHOICE D', '40.0'), ('CHOICE B', '45')], on_delete=django.db.models.deletion.CASCADE, to='first.commision_saraly'),
        ),
    ]