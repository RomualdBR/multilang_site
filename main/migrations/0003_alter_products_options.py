# Generated by Django 3.2.25 on 2024-06-20 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_example_products'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='products',
            options={'verbose_name': 'product'},
        ),
    ]