# Generated by Django 4.0.6 on 2023-08-10 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0073_dailywork_payement_method'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailywork',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='first.department'),
        ),
    ]
