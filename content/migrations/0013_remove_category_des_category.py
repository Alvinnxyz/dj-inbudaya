# Generated by Django 4.1.3 on 2022-11-23 08:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0012_budaya_isibudaya'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='des_category',
        ),
    ]
