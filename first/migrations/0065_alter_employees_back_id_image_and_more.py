# Generated by Django 4.0.6 on 2023-08-09 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0064_alter_employees_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='back_id_image',
            field=models.ImageField(blank=True, default='a.png', null=True, upload_to='upload/'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='front_id_image',
            field=models.ImageField(blank=True, default='a.png', null=True, upload_to='upload/'),
        ),
        migrations.AlterField(
            model_name='manager',
            name='profile_image',
            field=models.ImageField(blank=True, default='a.png', null=True, upload_to='upload/'),
        ),
    ]