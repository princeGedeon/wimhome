# Generated by Django 4.1 on 2024-02-27 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startup', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Magazine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('link', models.URLField()),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Partenaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('link', models.URLField()),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(default=' ', max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('commentaire', models.TextField(default='')),
                ('star', models.IntegerField(default=0)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
