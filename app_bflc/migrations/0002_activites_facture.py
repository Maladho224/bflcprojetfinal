# Generated by Django 5.2 on 2025-04-12 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_bflc', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photo')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Facture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('annee', models.CharField(max_length=50)),
                ('mois', models.CharField(max_length=50)),
                ('file', models.FileField(upload_to='photo')),
                ('commentaire', models.TextField()),
            ],
        ),
    ]
