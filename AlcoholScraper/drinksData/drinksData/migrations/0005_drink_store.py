# Generated by Django 4.2.2 on 2023-06-27 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drinksData', '0004_drink_sale_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='drink',
            name='store',
            field=models.CharField(default='LCBO'),
            preserve_default=False,
        ),
    ]