# Generated by Django 4.1.2 on 2022-10-11 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddDriverModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('driver_name', models.CharField(help_text='اسم السائق', max_length=225)),
                ('driver_nationality', models.CharField(help_text='جنسية السائق', max_length=225)),
                ('driver_phone_number', models.CharField(help_text='رقم هاتف السائق ', max_length=16)),
                ('Identification_Number', models.CharField(help_text='رقم الهوية/الاقامة', max_length=10)),
                ('truck_plate_number', models.CharField(help_text='رقم لوحة الشاحنة', max_length=8)),
                ('Vehicle_Type', models.CharField(help_text='نوع السيارة(سطحة - جوانب) ....', max_length=30)),
                ('Sequence_Number', models.CharField(help_text='الرقم التسلسلي من الاستمارة', max_length=30)),
                ('Owner_car_id_number', models.CharField(help_text='رقم هوية مالك السيارة', max_length=10)),
                ('Identification_photo', models.ImageField(help_text='صورة الهوية/الاقامة ', null=True, upload_to='driver/')),
                ('license_photo', models.ImageField(help_text=' صورة رخصة القيادة', null=True, upload_to='driver/')),
                ('Sequence_image', models.ImageField(help_text=' صورة من استمارة السيارة', null=True, upload_to='driver/')),
                ('car_picture', models.ImageField(help_text=' صورة جانبية او امامية للسيارة', null=True, upload_to='driver/')),
            ],
        ),
    ]
