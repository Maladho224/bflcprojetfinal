# Generated by Django 5.2 on 2025-04-13 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_bflc', '0003_activites_date_aj_albums_date_aj_facture_date_aj_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('subject', models.CharField(max_length=50)),
                ('message', models.TextField(max_length=500)),
            ],
        ),
    ]
