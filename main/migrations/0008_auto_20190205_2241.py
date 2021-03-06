# Generated by Django 2.0.1 on 2019-02-05 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20190203_2016'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_type',
            field=models.CharField(choices=[(0, 'General'), (1, 'Sketchbook'), (2, 'Exhibition'), (3, 'Teaching')], default=0, max_length=2),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='thumbnail',
            field=models.ImageField(blank=True, help_text='This will be the thumbnail for the project', null=True, upload_to='main/images/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='video',
            field=models.FileField(blank=True, help_text='This is the main video for the project', null=True, upload_to='main/videos/'),
        ),
    ]
