# Generated by Django 4.1.3 on 2022-12-30 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magicapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empadress',
            name='Country',
            field=models.CharField(choices=[('USA', 'India')], max_length=50),
        ),
    ]
