# Generated by Django 4.2.5 on 2023-10-19 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cartapp', '0003_rename_cartid_cart_cart_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='cart_id',
            new_name='cartid',
        ),
    ]