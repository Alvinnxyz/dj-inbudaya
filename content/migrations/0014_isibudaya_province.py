# Generated by Django 4.1.3 on 2022-11-23 08:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0013_remove_category_des_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='isibudaya',
            name='province',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='content.province'),
        ),
    ]