# Generated by Django 5.0.6 on 2024-06-14 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0008_alter_product_options_alter_version_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='version',
            old_name='linPortLink',
            new_name='linPortink',
        ),
        migrations.RenameField(
            model_name='version',
            old_name='linRPMLink',
            new_name='linRPMlink',
        ),
        migrations.RenameField(
            model_name='version',
            old_name='macOsLink',
            new_name='macOslink',
        ),
        migrations.RenameField(
            model_name='version',
            old_name='winExeLink',
            new_name='winExelink',
        ),
        migrations.RenameField(
            model_name='version',
            old_name='winMsiLink',
            new_name='winMsilink',
        ),
    ]
