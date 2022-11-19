# Generated by Django 4.1.3 on 2022-11-14 17:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('drivers', '0001_initial'),
        ('companies', '0001_initial'),
        ('financial', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoices',
            name='accountant',
        ),
        migrations.AddField(
            model_name='catchreceipt',
            name='accountant',
            field=models.CharField(max_length=225, null=True),
        ),
        migrations.AddField(
            model_name='invoices',
            name='auth',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='catchreceipt',
            name='company',
        ),
        migrations.RemoveField(
            model_name='catchreceipt',
            name='delegate',
        ),
        migrations.RemoveField(
            model_name='catchreceipt',
            name='driver',
        ),
        migrations.AddField(
            model_name='catchreceipt',
            name='company',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='companies.companymodel'),
        ),
        migrations.AddField(
            model_name='catchreceipt',
            name='delegate',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='catchreceipt',
            name='driver',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='drivers.drivermodel'),
        ),
    ]
