# Generated by Django 5.2 on 2025-04-13 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_bflc', '0005_message_date_aj'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commande',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('engins', models.CharField(max_length=50)),
                ('adres', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('date_aj', models.DateField(auto_now_add=True, null=True)),
            ],
        ),
    ]
