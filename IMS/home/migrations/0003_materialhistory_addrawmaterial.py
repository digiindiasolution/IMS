# Generated by Django 4.2.7 on 2024-02-19 10:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_unit'),
    ]

    operations = [
        migrations.CreateModel(
            name='MaterialHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rawmaterial_name', models.CharField(max_length=254)),
                ('quantity', models.PositiveIntegerField(blank=True, null=True)),
                ('category', models.CharField(max_length=200)),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.unit')),
                ('vendor_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.addvendor')),
            ],
        ),
        migrations.CreateModel(
            name='AddRawMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rawmaterial_name', models.CharField(max_length=254)),
                ('quantity', models.PositiveIntegerField(blank=True, null=True)),
                ('category', models.CharField(max_length=200)),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.unit')),
                ('vendor_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.addvendor')),
            ],
        ),
    ]
