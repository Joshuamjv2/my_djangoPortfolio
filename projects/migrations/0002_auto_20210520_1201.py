# Generated by Django 3.2.3 on 2021-05-20 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='git_repo',
            field=models.URLField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='project',
            name='live_site',
            field=models.URLField(blank=True, max_length=500),
        ),
    ]
