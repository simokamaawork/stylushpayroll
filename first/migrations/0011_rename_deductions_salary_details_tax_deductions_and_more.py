# Generated by Django 4.2.1 on 2023-06-05 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0010_commision_rate_remove_dailywork_job_type_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='salary_details',
            old_name='deductions',
            new_name='tax_deductions',
        ),
        migrations.RemoveField(
            model_name='salary_details',
            name='net_salary',
        ),
        migrations.AddField(
            model_name='salary_details',
            name='house_allowances',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='salary_details',
            name='medical_allowance',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='salary_details',
            name='provident_fund',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='employees',
            name='back_id_image',
            field=models.ImageField(default='a.png', upload_to='upload'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='front_id_image',
            field=models.ImageField(default='a.png', upload_to='upload'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='image',
            field=models.ImageField(default='a.png', upload_to='upload'),
        ),
    ]
