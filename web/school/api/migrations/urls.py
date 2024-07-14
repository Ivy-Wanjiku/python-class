from django.urls import path
from api.views import StudentListView

urlPatterns = [
    path("student/", StudentListView.as_view(), name="student_list_view"),
]