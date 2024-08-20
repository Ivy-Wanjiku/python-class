from django.urls import path
from .views import ClassPeriodDetailView, ClassPeriodListView, ClassroomDetailView, CourseDetailView, CourseListView, StudentListView, TeacherDetailView,TeacherListView, WeeklyTimetableView,StudentDetailView
urlpatterns = [
    path("students/", StudentListView.as_view(), name="student_list_view"),
    path('classperiod/', ClassPeriodListView.as_view(), name='classperiod_list_view'),
    path('course/', CourseListView.as_view(), name='course_list_view'),
    path('teacher/', TeacherListView.as_view(), name='teacher_list_view'),
    path("students/<int:id>/" ,StudentDetailView.as_view(),name="student_detail_view"),
    path("teacher/<int:id>/" ,TeacherDetailView.as_view(),name="teacher_detail_view"),
    path("classperiod/<int:id>/" ,ClassPeriodDetailView.as_view(),name="classperiod_detail_view"),
    path("course/<int:id>/" ,CourseDetailView.as_view(),name="course_detail_view"),
    path("weekly-timetable/", WeeklyTimetableView.as_view(),name="weekly-timetable"),
    path('classroom/<int:id>/', ClassroomDetailView.as_view(), name='classroom-detail_view'),


    

    

]