# Generated by Django 3.2.5 on 2021-07-09 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trailer', '0002_rename_poster_movie_poster_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='vote_count',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
