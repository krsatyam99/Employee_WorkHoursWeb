# Generated by Django 4.2.7 on 2023-11-17 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0003_alter_employee_details_hire_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee_details',
            name='Employee_Code',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
