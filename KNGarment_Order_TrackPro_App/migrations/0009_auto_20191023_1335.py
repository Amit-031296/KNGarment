# Generated by Django 2.2 on 2019-10-23 08:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('KNGarment_Order_TrackPro_App', '0008_auto_20191023_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='order_client_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='KNGarment_Order_TrackPro_App.Client'),
        ),
    ]
