# Generated by Django 3.2.5 on 2021-07-08 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('overview', models.CharField(blank=True, max_length=10, null=True)),
                ('poster', models.CharField(blank=True, max_length=4000, null=True)),
                ('vote_average', models.CharField(blank=True, max_length=20, null=True)),
                ('vote_count', models.SlugField(default='test')),
            ],
        ),
    ]
