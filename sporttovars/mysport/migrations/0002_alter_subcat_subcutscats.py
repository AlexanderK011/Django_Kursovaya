# Generated by Django 5.0.1 on 2024-02-05 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysport', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcat',
            name='subcutscats',
            field=models.ManyToManyField(blank=True, to='mysport.sport_item'),
        ),
    ]