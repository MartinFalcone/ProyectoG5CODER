# Generated by Django 4.0.4 on 2022-06-07 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0005_alter_product_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='purchase_date',
            new_name='created_at',
        ),
    ]
