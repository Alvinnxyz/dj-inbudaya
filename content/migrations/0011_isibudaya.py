# Generated by Django 4.1.3 on 2022-11-23 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0010_budaya'),
    ]

    operations = [
        migrations.CreateModel(
            name='IsiBudaya',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=100)),
                ('img_isibudaya', models.ImageField(blank=True, null=True, upload_to='gambar/')),
                ('des_isibudaya', models.TextField()),
            ],
        ),
    ]