# Generated by Django 4.1.2 on 2022-10-25 14:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('companies', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('drivers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShipmentModel',
            fields=[
                ('Shipment_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('destination', models.CharField(help_text=' الوجهة', max_length=225)),
                ('source', models.CharField(default='', help_text=' المصدر', max_length=225)),
                ('amount', models.CharField(help_text=' الاجرة', max_length=225)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('delivery_number', models.IntegerField()),
                ('status', models.CharField(help_text=' phgm hgapkm', max_length=225)),
                ('company', models.ManyToManyField(to='companies.companymodel')),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drivers.drivermodel')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
