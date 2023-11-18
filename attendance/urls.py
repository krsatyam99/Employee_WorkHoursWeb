
from django.urls import path
from attendance import views
# from attendance.views import 





urlpatterns = [
 
  
    path("testing/", views.testing),
    path("employe_info/", views.employee_info, name='employe_info'),
    path("add_employee/", views.create, name='add_employee'),
    path("del_employee/<int:id>", views.delete_employee, name='del_employee'),
    path("update/<int:id>", views.update, name='update'),
    path("attend/",views.attendance_report, name ="attend"),
    path("excel/",views.generate_and_download_excel, name ="excel"),
    path("data/",views.get_attendance_data, name='data')







]
