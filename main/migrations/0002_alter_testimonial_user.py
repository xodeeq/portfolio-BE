# Generated by Django 3.2.8 on 2021-10-22 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='user',
            field=models.CharField(max_length=40),
        ),
    ]
