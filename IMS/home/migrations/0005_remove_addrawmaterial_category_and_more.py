# Generated by Django 4.2.7 on 2024-02-20 05:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_addrawmaterial_unit_alter_materialhistory_unit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addrawmaterial',
            name='category',
        ),
        migrations.RemoveField(
            model_name='materialhistory',
            name='category',
        ),
    ]
