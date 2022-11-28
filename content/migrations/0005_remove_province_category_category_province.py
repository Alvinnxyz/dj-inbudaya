# Generated by Django 4.0.6 on 2022-11-19 08:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0004_province_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='province',
            name='category',
        ),
        migrations.AddField(
            model_name='category',
            name='province',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='content.province'),
        ),
    ]
