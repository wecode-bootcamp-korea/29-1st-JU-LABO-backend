# Generated by Django 4.0.1 on 2022-01-28 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='categoryjoin',
            new_name='categorysubcategory_id',
        ),
    ]