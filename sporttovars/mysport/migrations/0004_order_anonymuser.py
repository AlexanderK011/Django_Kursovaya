# Generated by Django 5.0.1 on 2024-03-12 15:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysport', '0003_alter_anonymcustomer_city_alter_user_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='anonymuser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mysport.anonymcustomer'),
        ),
    ]