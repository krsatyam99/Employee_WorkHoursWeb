from django.db import models
from datetime import date
from datetime import timedelta


class employee_details(models.Model):
    DESIGNATION_CHOICES = [
        ('IN', 'Intern'),
        ('FR', 'Fresher'),
        ('TL', 'Team Lead'),
        ('M', 'Manager'),
        ('SM', 'Senior Manager'),
    ]

    DEPARTMENT_CHOICES = [
        ('SA', 'Sales'),
        ('MA', 'Marketing'),
        ('HR', 'HR'),
        ('DEV', 'Developers'),
        ('CC', 'Customer Care'),
        ('CE', 'Cloud Engineers'),
    ]

    Employee_Code = models.CharField(max_length=20, unique=False, editable=True)
    First_Name = models.CharField(max_length=50)
    Last_Name = models.CharField(max_length=50)
    Full_Name = models.CharField(max_length=100, editable=False, null=True)
    Hire_Date = models.DateField(db_index=True)
    Designation = models.CharField(max_length=2, choices=DESIGNATION_CHOICES)
    Department = models.CharField(max_length=3, choices=DEPARTMENT_CHOICES)

  


    def save(self, *args, **kwargs):
        if not self.Employee_Code:
            # Generating employee code based on Designation and Department
            designation_code = self.Designation[-2:] if self.Designation else ''
            department_code = self.Department[-2:] if self.Department else ''

            # Counting existing employees with the same designation and department
            existing_count = employee_details.objects.filter(Designation=self.Designation, Department=self.Department).count()

            # Generating Employee_Code
            if designation_code and department_code:  # Ensure that these codes have values
                if self.id is not None:  # Check if it's an existing instance
                    self.Employee_Code = f'{designation_code}{department_code}updated{existing_count + 1}'
                else:
                    self.Employee_Code = f'{designation_code}{department_code}{existing_count + 1}'

        if not self.Full_Name:
            self.Full_Name = f'{self.First_Name} {self.Last_Name}'

        super().save(*args, **kwargs)  # Calling the parent class with super()

    def __str__(self):
        return f'{self.Employee_Code} - {self.Full_Name}'
    




class AttendanceTransaction(models.Model):
    employee = models.ForeignKey(employee_details, on_delete=models.CASCADE)
    first_punch_date = models.DateField(default=date.today)  # Set default to today's date
    first_punch_time = models.TimeField(unique=True)
    last_punch_time = models.TimeField(unique=True)
    leaves_in_the_month =models.CharField(max_length=40)
    total_hour_working = models.DurationField(editable=False)

    def save(self, *args, **kwargs):
        # Set first_punch_date to today's date if not already set
        if not self.first_punch_date:
            self.first_punch_date = date.today()

        # Check if first_punch_time is being set for the first time on the given day
        existing_first_punch = AttendanceTransaction.objects.filter(
            employee=self.employee,
            first_punch_date=self.first_punch_date
        ).exclude(pk=self.pk)  # Exclude the current instance if updating

        if existing_first_punch.exists():
            # If a record already exists for the same day, raise an exception or handle accordingly
            raise ValueError('First punch already registered for the day.')
        
        # Check if last_punch_time is being set for the first time on the given day
        existing_last_punch = AttendanceTransaction.objects.filter(
            employee=self.employee,
            first_punch_date=self.first_punch_date,
        ).exclude(pk=self.pk)  # Exclude the current instance if updating

        if existing_last_punch.exists():
            # If a record already exists for the same day, raise an exception or handle accordingly
            raise ValueError('Last punch already registered for the day.')
        time_difference = timedelta(hours=self.last_punch_time.hour, minutes=self.last_punch_time.minute) - timedelta(hours=self.first_punch_time.hour, minutes=self.first_punch_time.minute)
        self.total_hour_working = time_difference
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.employee.Employee_Code} - {self.first_punch_date} {self.first_punch_time}'

