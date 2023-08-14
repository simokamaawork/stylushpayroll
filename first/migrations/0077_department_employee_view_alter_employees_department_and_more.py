# Generated by Django 4.0.6 on 2023-08-14 12:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0076_daily_results_employee_initializer_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='department_employee_view',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.AlterField(
            model_name='employees',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employees', to='first.department'),
        ),
        migrations.CreateModel(
            name='debit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('month', models.DateTimeField(auto_now_add=True)),
                ('reason', models.TextField(blank=True)),
                ('employee_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first.employees')),
            ],
        ),
    ]