# Generated by Django 4.2.4 on 2023-08-28 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0006_alter_product_seller'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
