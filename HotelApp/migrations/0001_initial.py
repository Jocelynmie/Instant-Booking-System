

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Authorregis',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Fname', models.CharField(max_length=255)),
                ('Lname', models.CharField(max_length=255)),
                ('Email', models.CharField(max_length=255, unique=True)),
                ('Phone_Number', models.IntegerField()),
                ('Password', models.CharField(max_length=255)),
                ('Date', models.DateField(auto_now_add=True)),
                ('Time', models.TimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'Authority_reg',
            },
        ),
    ]
