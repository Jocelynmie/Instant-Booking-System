
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HotelApp', '0004_add_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_employee',
            name='Email',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='add_employee',
            name='Mobile_Number',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='add_employee',
            name='Personal_Identity',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
