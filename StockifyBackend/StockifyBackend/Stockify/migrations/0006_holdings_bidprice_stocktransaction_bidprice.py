# Generated by Django 4.1.4 on 2023-03-22 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Stockify', '0005_remove_holdings_bidprice_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='holdings',
            name='bidPrice',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='stocktransaction',
            name='bidPrice',
            field=models.FloatField(default=0),
        ),
    ]
