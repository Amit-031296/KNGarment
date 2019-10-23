# Generated by Django 2.2 on 2019-10-23 04:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('KNGarment_Order_TrackPro_App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fabric_Order',
            fields=[
                ('process_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='KNGarment_Order_TrackPro_App.Process')),
                ('fabric_order_sort_number', models.CharField(max_length=920)),
                ('fabric_order_quantity', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Fabric Order',
                'verbose_name_plural': 'Fabric Orders List',
            },
            bases=('KNGarment_Order_TrackPro_App.process',),
        ),
    ]
