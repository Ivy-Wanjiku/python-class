from datetime import timedelta, timezone
from django.shortcuts import render
from rest_framework.views import APIView
from classperiod.models import ClassPeriod
from classroom.models import Classroom
from course.models import Course
from student.models import Student
from teacher.models import Teacher
from rest_framework import status
from .serializers import ClassPeriodSerializer, StudentSerializer, CourseSerializer, TeacherSerializer,ClassroomSerializer
from rest_framework.response import Response

class StudentListView(APIView):
    def get(self,request):
        students=Student.objects.all()
        first_name=request.query_params.get("first_name")
        nationality=request.query_params.get("nationality")
        if first_name:
            students=students.filter(first_name=first_name)
        if nationality:
            students=students.filter(nationality=nationality)
        serializer=StudentSerializer(students,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class StudentDetailView(APIView):
    def enroll_student(self,student,course_code):
        course=Course.objects.get(id=course_code)
        student.course.add(course)
    def post(self,request,id):
        student=Student.objects.get(id=id)
        action=request.data.get("action")
        if action=="enroll":
            course_code=request.data.get("course")
            student_id=request.data.get("Student")
            student=Student.objects.get(id=student_id)
            self.enroll_student(student,course_code)
            return  Response(status.HTTP_201_CREATED)
    def get(self,request,id):
        student=Student.objects.get(id=id)
        serializer=StudentSerializer(student)
        return Response(serializer.data)
    
    def put (self,request,id):
        student=Student.objects.get(id=id)
        serializer=StudentSerializer(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id):
        student=Student.objects.get(id=id)
        student.delete()
        return Response (status=status.HTTP_202_ACCEPTED)
    
class ClassPeriodListView(APIView):
    def get(self, request):
        classsperiod=ClassPeriod.objects.all
        serializer = ClassPeriodSerializer(classsperiod, many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=ClassPeriodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class ClassPeriodDetailView(APIView):
    def get(self,request,id):
        classperiod=ClassPeriod.objects.get(id=id)
        serializer=ClassPeriodSerializer(classperiod)
        return Response(serializer.data)
    
    def put (self,request,id):
        classperiod=ClassPeriod.objects.get(id=id)
        serializer=ClassPeriodSerializer(classperiod,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id):
        classperiod=ClassPeriod.objects.get(id=id)
        classperiod.delete()
        return Response (status=status.HTTP_202_ACCEPTED)
class CourseListView(APIView):
    def get(self, request):
        serializer = CourseSerializer(Course.objects.all(), many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class CourseDetailView(APIView):
    def get(self,request,id):
        course=Course.objects.get(id=id)
        serializer=CourseSerializer(course)
        return Response(serializer.data)
    
    def put (self,request,id):
        course=Course.objects.get(id=id)
        serializer=CourseSerializer(course,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id):
        course=Course.objects.get(id=id)
        Course.delete()
        return Response (status=status.HTTP_202_ACCEPTED)
    def post(self,request,id):
        course=Course.objects.get(id=id)
        action=request.data.get("action")
        if action =="assign_teacher":
            teacher_id=request.data.get("teacher")
            teacher=Teacher.objects.get(id=teacher_id)
            course.teacher.add(teacher)
            return Response ({"status":"teacher assigned"} , status=status.HTTP_201_CREATED)
        return Response ({"error":"invalid action"},status=status.HTTP_400_BAD_REQUEST)
class TeacherListView(APIView):
    def get(self, request):
        serializer = TeacherSerializer(Teacher.objects.all(), many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class TeacherDetailView(APIView):
    def get(self,request,id):
        teacher=Teacher.objects.get(id=id)
        serializer=TeacherSerializer(Teacher)
        return Response(serializer.data)
    
    def put (self,request,id):
        teacher=Teacher.objects.get(id=id)
        serializer=TeacherSerializer(Teacher,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id):
        teacher=Teacher.objects.get(id=id)
        teacher.delete()
        return Response (status=status.HTTP_202_ACCEPTED)
class WeeklyTimetableView(APIView):
    def get(self,request):
        now=timezone.now()
        start_of_week =now -timedelta(days=now.weekday())
        end_of_week =start_of_week + timedelta(days=6)

        timetable_data ={
            "start_of_week":start_of_week.isoformat(),
            "end_of_week":end_of_week.isoformat(),
            }
        return Response(timetable_data,status=status.HTTP_200_OK)

class ClassroomDetailView(APIView):
    def get(self, request, id):
        classroom = Classroom.objects.get(id=id)
        serializer = ClassroomSerializer(classroom)
        return Response(serializer.data)
    def put(self, request, id):
        classroom = Classroom.objects.get(id=id)
        serializer = ClassroomSerializer(classroom, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        classroom = Classroom.objects.get(id=id)
        classroom.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    def post(self, request, id):
        classroom = Classroom.objects.get(id=id)
        action = request.data.get("action")
        if action == "add_student":
            student_id = request.data.get("student")
            student = Student.objects.get(id=student_id)
            classroom.students.add(student)
            return Response({"status": "student added"}, status=status.HTTP_201_CREATED)
        return Response({"error": "invalid action"}, status=status.HTTP_400_BAD_REQUEST)

