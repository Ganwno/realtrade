# Generated by Django 4.0.3 on 2023-03-20 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Stockify', '0002_stocktransaction_holdings'),
    ]

    operations = [
        migrations.AddField(
            model_name='holdings',
            name='bidPrice',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
