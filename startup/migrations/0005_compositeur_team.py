# Generated by Django 4.1 on 2024-02-28 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startup', '0004_magazine_img_partenaire_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compositeur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='Teams')),
                ('nom', models.CharField(max_length=300)),
                ('title', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('link', models.URLField(default='a.com')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='Teams')),
                ('nom', models.CharField(max_length=300)),
                ('title', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('link', models.URLField(default='a.com')),
            ],
        ),
    ]
