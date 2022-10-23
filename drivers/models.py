from django.db import models

# Create your models here.
class DriverModel(models.Model):
    driver_id = models.BigAutoField(primary_key=True)
    driver_name = models.CharField(max_length=225,  help_text='اسم السائق')
    driver_nationality = models.CharField(max_length=225,  help_text='جنسية السائق')
    driver_phone_number = models.CharField( max_length=16, help_text='رقم هاتف السائق ')
    Identification_Number = models.CharField(max_length=10,  help_text='رقم الهوية/الاقامة')
    truck_plate_number = models.CharField(max_length=8,  help_text='رقم لوحة الشاحنة')
    Vehicle_Type = models.CharField(max_length=30, help_text='نوع السيارة(سطحة - جوانب) ....')
    Sequence_Number	 = models.CharField(max_length=30, help_text='الرقم التسلسلي من الاستمارة')
    Owner_car_id_number = models.CharField(max_length=10,  help_text='رقم هوية مالك السيارة')
    Identification_photo = models.ImageField(upload_to='driver/', null=True, help_text='صورة الهوية/الاقامة ')
    # license_photo = models.ImageField(upload_to='driver/', null=True, help_text=' صورة رخصة القيادة')
    # Sequence_image = models.ImageField(upload_to='driver/', null=True, help_text=' صورة من استمارة السيارة')
    # car_picture = models.ImageField(upload_to='driver/', null=True, help_text=' صورة جانبية او امامية للسيارة')


    def __str__(self):
        return self.driver_name

