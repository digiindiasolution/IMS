# Generated by Django 4.2.7 on 2024-02-20 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_remove_addrawmaterial_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='materialhistory',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]