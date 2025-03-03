from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashbord"),
    path("add-student/", views.add_student, name="add_student"),
    path("list-student/", views.student_list, name="list_student"),
]
