from django.urls import path
from . import views

urlpatterns = [
    path('', views.Login, name='login'),
    path('home',views.Home, name='home'),
    path('register/', views.Register, name='register'),
    path('allteachers/', views.allTeachers, name='allteachers'),
    path('allstudents/', views.allStudents, name='allstudents'),
    path('allexams/', views.allExams, name='allexams'),
    path('alltests/', views.allTests, name='alltests'),

    path('addstudent/', views.addStudent, name='addstudent'),
    path('addteacher/', views.addTeacher, name='addteacher'),
    path('addexam/', views.addExam, name='addexam'),
    path('addtest/', views.addTest, name='addtest'),

    path('updatestudent/<str:pk>', views.updateStudent, name='updatestudent'),
    path('updateteacher/<str:pk>', views.updateTeacher, name='updateteacher'),
    path('examedit/<str:pk>', views.examEdit, name='examedit'),
    path('testedit/<str:pk>', views.testEdit, name='testedit'),
    path('deleteteacher/<str:pk>', views.deleteTeacher, name='deleteteacher'),
    path('deletestudent/<str:pk>', views.deleteStudent, name='deletestudent'),
]