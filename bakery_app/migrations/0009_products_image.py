# Generated by Django 5.0.4 on 2024-04-29 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bakery_app', '0008_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
