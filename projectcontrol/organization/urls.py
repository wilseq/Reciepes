from django.urls import path
from . import views






urlpatterns = [
    path('students/', views.students, name='students'),
    path('employee/', views.employee, name='employee'),
    path('emplistview/', views.emp_list_view, name='emp_list_view'),
    path('studlistview/', views.stud_list_view, name='stud_list_view'),
    #path('',include('acount.urls')),
    #path('register/', registration_view, name= 'register'),
    #path('logout/', logout_view, name="logout"),
]