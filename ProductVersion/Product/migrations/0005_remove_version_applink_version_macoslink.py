# Generated by Django 5.0.6 on 2024-06-11 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0004_remove_version_linlink_remove_version_winlink_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='version',
            name='AppLink',
        ),
        migrations.AddField(
            model_name='version',
            name='MacOsLink',
            field=models.CharField(max_length=50, null=True, verbose_name='MacOs Version'),
        ),
    ]
