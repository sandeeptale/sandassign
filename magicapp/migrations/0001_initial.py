# Generated by Django 4.1.3 on 2022-12-30 12:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmpAdress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Schedule_On', models.DateField(auto_created=True)),
                ('Massage', models.TextField(max_length=160)),
                ('Email', models.EmailField(max_length=25, unique=True)),
                ('Country', models.CharField(max_length=50)),
                ('Phone', models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(10, 'the field must contain at least 10 characters')])),
            ],
        ),
    ]
