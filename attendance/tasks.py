from celery import shared_task
from time import sleep
import logging





from django.db.models import Count
from .models import AttendanceTransaction  # Import your model
logger = logging.getLogger(__name__)


@shared_task
def print_days_worked():
    try:
        employee_ids = AttendanceTransaction.objects.values_list('employee_id', flat=True).distinct()
        employee_data = {}

        for employee_id in employee_ids:
            days_worked_data = (
                AttendanceTransaction.objects
                .filter(employee_id=employee_id)
                .values('employee__Full_Name', 'employee__Employee_Code', 'first_punch_date')
                .annotate(total_occurrences=Count('first_punch_date'))
            )

            total_occurrences = sum(entry['total_occurrences'] for entry in days_worked_data)

            print(f'Total days worked for employee {employee_id}: {total_occurrences} occurrences')



            employee_data[employee_id] = {
                'Full_Name': days_worked_data[0]['employee__Full_Name'],
                'Employee_Code': days_worked_data[0]['employee__Employee_Code'],
                'total_occurrences': total_occurrences,
                'days_worked_data': days_worked_data,
            }

    except Exception as e:
        logger.error(f'Error in print_days_worked task: {e}', exc_info=True)


# Use the Celery task to print the data every 1 minute
@shared_task
def sleepy(duration):
    sleep(duration)
    print_days_worked.delay()
    return None
