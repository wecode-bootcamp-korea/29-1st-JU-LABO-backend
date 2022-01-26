# Generated by Django 4.0.1 on 2022-01-26 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('img_url', models.URLField(max_length=1000)),
            ],
            options={
                'db_table': 'productgroups',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('ml', models.IntegerField()),
                ('description', models.CharField(max_length=500)),
                ('inventory', models.IntegerField()),
                ('is_default', models.BooleanField(default=False)),
                ('categoryjoin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categories.categoryjoin')),
                ('productgroup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.productgroup')),
            ],
            options={
                'db_table': 'products',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_url', models.URLField(max_length=1000)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
            options={
                'db_table': 'images',
            },
        ),
    ]
