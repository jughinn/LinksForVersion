# Generated by Django 5.0.6 on 2024-06-11 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0003_alter_version_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='version',
            name='LinLink',
        ),
        migrations.RemoveField(
            model_name='version',
            name='WinLink',
        ),
        migrations.AddField(
            model_name='version',
            name='LinPortLink',
            field=models.CharField(max_length=50, null=True, verbose_name='Linux Version Portable'),
        ),
        migrations.AddField(
            model_name='version',
            name='LinRPMLink',
            field=models.CharField(max_length=50, null=True, verbose_name='Linux Version RPM'),
        ),
        migrations.AddField(
            model_name='version',
            name='WinExeLink',
            field=models.CharField(max_length=50, null=True, verbose_name='Windows Version Exe'),
        ),
        migrations.AddField(
            model_name='version',
            name='WinMsiLink',
            field=models.CharField(max_length=50, null=True, verbose_name='Windows Version MSI'),
        ),
    ]
