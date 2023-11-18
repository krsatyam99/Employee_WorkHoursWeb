# Generated by Django 4.2.7 on 2023-11-17 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employee_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Employee_Code', models.CharField(editable=False, max_length=20, unique=True)),
                ('First_Name', models.CharField(max_length=50)),
                ('Last_Name', models.CharField(max_length=50)),
                ('Hire_Date', models.DateField()),
                ('Designation', models.CharField(choices=[('IN', 'Intern'), ('FR', 'Fresher'), ('TL', 'Team Lead'), ('M', 'Manager'), ('SM', 'Senior Manager')], max_length=2)),
                ('Department', models.CharField(choices=[('SA', 'Sales'), ('MA', 'Marketing'), ('HR', 'HR'), ('DEV', 'Developers'), ('CC', 'Customer Care'), ('CE', 'Cloud Engineers')], max_length=3)),
            ],
        ),
    ]
