# Generated by Django 4.1.3 on 2022-12-31 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magicapp', '0005_alter_empadress_country_alter_empadress_massage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empadress',
            name='Country',
            field=models.CharField(choices=[('INDIA', 'INDIA'), ('USA', 'USA')], max_length=50),
        ),
    ]
