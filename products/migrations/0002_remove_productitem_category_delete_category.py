# Generated by Django 4.1.1 on 2022-12-16 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productitem',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]