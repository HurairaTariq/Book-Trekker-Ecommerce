# Generated by Django 4.0.1 on 2022-06-17 17:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0012_product_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productupload',
            name='customer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ecomapp.customer'),
            preserve_default=False,
        ),
    ]
