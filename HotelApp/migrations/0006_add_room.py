

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HotelApp', '0005_auto_20210713_2205'),
    ]

    operations = [
        migrations.CreateModel(
            name='Add_Room',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Room_Number', models.CharField(max_length=255, unique=True)),
                ('Room_Type', models.CharField(max_length=255)),
                ('Room_Floor', models.CharField(max_length=255)),
                ('Room_Facility', models.CharField(max_length=500)),
                ('Room_Price', models.CharField(max_length=255)),
                ('Room_Image', models.ImageField(upload_to='')),
                ('Date', models.DateField(auto_now_add=True)),
                ('Time', models.TimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'Add_Room',
            },
        ),
    ]
