# Generated by Django 4.0.6 on 2023-08-09 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0067_alter_employees_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='image',
            field=models.ImageField(blank=True, default='a.png', null=True, upload_to='upload/'),
        ),
    ]
