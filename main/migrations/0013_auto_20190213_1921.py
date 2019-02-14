# Generated by Django 2.0.1 on 2019-02-13 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_project_date_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='banner',
            field=models.ImageField(blank=True, help_text='This will be the banner for the project', null=True, upload_to='main/images/banners/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='date_field',
            field=models.DateField(),
        ),
    ]
