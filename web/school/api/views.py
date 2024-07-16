from django.shortcuts import render
from rest_framework.views import APIView
from classperiod.models import ClassPeriod
from course.models import Course
from student.models import Student
from teacher.models import Teacher
from .serializers import ClassPeriodSerializer, StudentSerializer, CourseSerializer
from rest_framework.response import Response

class StudentListView(APIView):
    def get(self,request):
        students=Student.objects.all()
        serializer=StudentSerializer(students,many=True)
        return Response(serializer.data)

class ClassPeriodListView(APIView):
    def get(self, request):
        classsperiod=ClassPeriod.objects.all
        serializer = ClassPeriodSerializer(classsperiod, many=True)
        return Response(serializer.data)
class CourseListView(APIView):
    def get(self, request):
        serializer = CourseSerializer(Course.objects.all(), many=True)
        return Response(serializer.data)

class TeacherListView(APIView):
    def get(self, request):
        serializer = CourseSerializer(Teacher.objects.all(), many=True)
        return Response(serializer.data)
