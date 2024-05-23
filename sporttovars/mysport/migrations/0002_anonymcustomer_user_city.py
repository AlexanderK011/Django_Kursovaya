# Generated by Django 5.0.1 on 2024-03-12 15:42

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysport', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnonymCustomer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('number_phone', models.CharField(max_length=25)),
                ('city', models.CharField(max_length=35)),
                ('address', models.CharField(max_length=200, null=True)),
                ('postal_index', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.CharField(default=django.utils.timezone.now, max_length=35),
            preserve_default=False,
        ),
    ]