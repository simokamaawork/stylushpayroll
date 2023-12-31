# Generated by Django 4.2.1 on 2023-05-25 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0003_adddepartment_addexpenses_advancesalary_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyWork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.FloatField()),
                ('employee_name', models.CharField(max_length=255)),
                ('total_amount', models.FloatField(max_length=255)),
                ('job_type', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='overtime',
            name='Hour',
            field=models.DurationField(),
        ),
        migrations.AlterField(
            model_name='overtime',
            name='Text',
            field=models.TextField(),
        ),
    ]
