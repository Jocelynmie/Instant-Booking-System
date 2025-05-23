

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HotelApp', '0002_online_booking'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offline_Booking',
            fields=[
                ('Customer_Id', models.AutoField(primary_key=True, serialize=False)),
                ('Check_in', models.CharField(max_length=255)),
                ('Check_out', models.CharField(max_length=255)),
                ('First_Name', models.CharField(max_length=255)),
                ('Last_Name', models.CharField(max_length=255)),
                ('Email', models.CharField(max_length=255)),
                ('Mobile_Number', models.IntegerField()),
                ('ADULT', models.CharField(max_length=255)),
                ('CHILDREN', models.CharField(max_length=255)),
                ('Total_Person', models.IntegerField()),
                ('Select_Room', models.CharField(max_length=255)),
                ('Room_Number', models.CharField(max_length=255)),
                ('Gender', models.CharField(max_length=255)),
                ('Personal_Identity', models.CharField(max_length=255)),
                ('Upload_Image', models.ImageField(upload_to='')),
                ('Country', models.CharField(max_length=255)),
                ('Address', models.CharField(max_length=255)),
                ('Date', models.DateField(auto_now_add=True)),
                ('Time', models.TimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'Offline_Booking_Customer',
            },
        ),
    ]
