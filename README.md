# Employee_WorkHoursWeb

This web application is designed to efficiently manage employee information, facilitate the addition of new employees, and streamline attendance tracking.

- [Demo Link](#demo-link)
- [LinkedIn](https://www.linkedin.com/in/kumar-satyam-769340243/)
## Table of Contents

1. [Employee_WorkHoursWeb](#employee_workhoursweb)
    - [Problem Statements](#problem-statements)
        - [Task 1: Employee Details Management Interface](#task-1-employee-details-management-interface)
        - [Task 2: Employee Attendance Tracking](#task-2-employee-attendance-tracking)
        - [Task 3: Real-time Attendance Report](#task-3-real-time-attendance-report)
    - [Sequence Diagram for Web App](#sequence-diagram-for-web-app)
    - [Prerequisites](#prerequisites)
        - [Libraries Used](#libraries-used)
    - [Additional Features](#additional-features)
    - [Task 1: Employee Details Management Interface](#task-1-employee-details-management-interface-1)
    - [Task 2: Employee Attendance Tracking](#task-2-employee-attendance-tracking-1)
    - [Task 3: Real-time Attendance Report](#task-3-real-time-attendance-report-1)
    -  [Diagram for Celery Integration and Admin Panel](#diagram-for-celery-integration-and-admin-panel)



## Problem Statements

Task 1: Create an interface for adding, listing, deleting, and updating employee details. The details should include Employee Code, First Name, Last Name, and Hire Date.

Task 2: Develop an interface to add employee attendance transaction like Punch time ,date,,employee code punch time should be unique and restrict to enter duplicate punch time

Task 3: Create a report that displays an employee's first punch and last punch based on real-time attendance transactions. Utilize a Celery task to calculate attendance.

## Sequence Diagram for Web App
![celery](https://github.com/krsatyam99/Employee_WorkHoursWeb/assets/103446420/0596bca1-2913-4e92-b6d4-9c03c9f93bd9)


## Prerequisites

- Python
- Django
- HTML
- CSS
- JavaScript

### Libraries Used

- Celery
- Celery Beats
- Redis
- Eventlet
- Openpyxl

## Additional Features
- Daily attendance reports for individual employees are available.
 [attendance_data (6).xlsx](https://github.com/krsatyam99/Employee_WorkHoursWeb/files/13400397/attendance_data.6.xlsx)

- Users can access comprehensive attendance reports for each employee.

  [attendance_report (2).xlsx](https://github.com/krsatyam99/Employee_WorkHoursWeb/files/13400405/attendance_report.2.xlsx)

## Task 1: Employee Details Management Interface

![Screenshot (12)](https://github.com/krsatyam99/Employee_WorkHoursWeb/assets/103446420/8ed390f1-7601-4344-a158-fcf227edd220)

![Screenshot (13)](https://github.com/krsatyam99/Employee_WorkHoursWeb/assets/103446420/9cc46523-e2ba-44c0-a3d3-36950fcf193b)


## Task 2:Adding attendance

![Screenshot (15)](https://github.com/krsatyam99/Employee_WorkHoursWeb/assets/103446420/44761e1e-e6df-4f1e-b03f-ad1585f753e2)

## Task 3: Employee Attendance Tracking
![Screenshot (14)](https://github.com/krsatyam99/Employee_WorkHoursWeb/assets/103446420/9b8f2b01-d845-4a67-84d6-960604d5fa50)

...




## Diagram for Celery Integration and  Admin panel
### Admin Panel 
![Screenshot (16)](https://github.com/krsatyam99/Employee_WorkHoursWeb/assets/103446420/4f8fe88e-f14a-44eb-a7eb-37375a2ce87c)

![Screenshot (17)](https://github.com/krsatyam99/Employee_WorkHoursWeb/assets/103446420/1baf3c15-8238-4d79-8ca3-a48c0a7728cb)

 ### General  Architecture


![iiii](https://github.com/krsatyam99/Employee_WorkHoursWeb/assets/103446420/1e7dc066-773d-4ab5-87d7-a5456d182157)



...




