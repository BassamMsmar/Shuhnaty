from datetime import date
from email.policy import default
from django.db import models
from django.utils import timezone

from drivers.models import DriverModel
from companies.models import CompanyModel
from accounts.forms import User

# Create your models here.

class ShipmentModel(models.Model):
    Shipment_id = models.BigAutoField(primary_key=True)
    driver = models.ForeignKey(DriverModel, on_delete=models.CASCADE)
    company = models.ManyToManyField(CompanyModel)
    destination =  models.CharField(max_length=225,  help_text=' الوجهة')
    source =  models.CharField(max_length=225,  help_text=' المصدر')
    amount =  models.CharField(max_length=225,  help_text=' الاجرة')
    employee =  models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    delivery_number = models.IntegerField()
    status = models.CharField(max_length=225,  help_text=' phgm hgapkm')




    def __str__(self):
        return self.driver.driver_name


