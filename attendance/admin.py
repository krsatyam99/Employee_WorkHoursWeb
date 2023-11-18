from django.contrib import admin
from attendance.models import *

# Register your models here.
class Employee_admin(admin.ModelAdmin):
    list_display=('id','Employee_Code','Hire_Date','Full_Name')
    ordering = ('Hire_Date',)
admin.site.register(employee_details,Employee_admin)



class Employee_attendance(admin.ModelAdmin):
    list_display = ('id', 'get_full_name', 'first_punch_time', 'last_punch_time', 'total_hour_working')
    ordering = ('first_punch_date',)

    def get_full_name(self, obj):
        return obj.employee.Full_Name

    get_full_name.short_description = 'Employee Full Name'

admin.site.register(AttendanceTransaction, Employee_attendance)