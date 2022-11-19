# Generated by Django 4.1.3 on 2022-11-14 17:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('drivers', '0001_initial'),
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CatchReceipt',
            fields=[
                ('catchReceipt_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('source', models.CharField(default='', help_text=' المصدر', max_length=225)),
                ('destination', models.CharField(help_text=' الوجهة', max_length=225)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('amount', models.CharField(help_text=' الاجرة', max_length=225)),
                ('overnight', models.CharField(help_text=' المبات', max_length=225)),
                ('return_fare', models.CharField(help_text=' اجرة رجعة', max_length=225)),
                ('deduction', models.CharField(help_text='خصم', max_length=225)),
                ('policy_number', models.CharField(default='', help_text=' رقم البوليصة', max_length=225)),
                ('notice_number', models.CharField(default='', help_text=' رقم الاشعار', max_length=225)),
                ('Shipment_id', models.CharField(default='', help_text=' رقم الشحن', max_length=225)),
                ('company', models.ManyToManyField(to='companies.companymodel')),
                ('delegate', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('driver', models.ManyToManyField(to='drivers.drivermodel')),
            ],
        ),
        migrations.CreateModel(
            name='Invoices',
            fields=[
                ('invoices_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('CatchReceipt', models.ManyToManyField(to='financial.catchreceipt')),
                ('accountant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]