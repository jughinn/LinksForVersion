# Generated by Django 5.0.6 on 2024-06-10 15:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.CharField(max_length=50, verbose_name='Version')),
                ('LinLink', models.CharField(max_length=50, verbose_name='LinuxVersion')),
                ('WinLink', models.CharField(max_length=50, verbose_name='WindowsVersion')),
                ('AppLink', models.CharField(max_length=50, verbose_name='AppleVersion')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='version', to='Product.product')),
            ],
        ),
    ]
