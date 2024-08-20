
from datetime import timedelta, timezone
from django.shortcuts import render
from rest_framework.views import APIView
from classperiod.models import ClassPeriod
from classroom.models import Classroom
from course.models import Course
from student.models import Student
from teacher.models import Teacher
from rest_framework import status
from .serializers import ClassPeriodSerializer, MinimalCourseSerializer, MinimalTeacherSerializer, StudentSerializer, CourseSerializer, TeacherSerializer,ClassroomSerializer,MinimalStudentSerializer
from rest_framework.response import Response


class StudentListView(APIView):
    def get(self, request):
        students = Student.objects.all()
        first_name = request.query_params.get("first_name")
        nationality = request.query_params.get("nationality")
        if first_name:
            students = students.filter(first_name=first_name)
        if nationality:
            students = students.filter(nationality=nationality)
        serializer = MinimalStudentSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentDetailView(APIView):
    def enroll_student(self, student, course):
        student.courses.add(course)

    def post(self, request, id):
        student = Student.objects.get(id=id)
        action = request.data.get("action")
        if action == "enroll":
            course_id = request.data.get("course")
            course = Course.objects.get(id=course_id)
            self.enroll_student(student, course)
            return Response(status=status.HTTP_201_CREATED)
        return Response({"error": "Invalid action"}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id):
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def put(self, request, id):
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        student = Student.objects.get(id=id)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ClassPeriodListView(APIView):
    def get(self, request):
        end_time = request.query_params.get("end_time")
        start_time = request.query_params.get("start_time")
        if end_time:
            classperiod = classperiod.filter(first_name=end_time)
        if start_time:
            students = students.filter()
        serializer = MinimalStudentSerializer(students, many=True)
        return Response(serializer.data)



    def post(self, request):
        serializer = ClassPeriodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClassPeriodDetailView(APIView):
    def get(self, request, id):
        class_period = ClassPeriod.objects.get(id=id)
        serializer = ClassPeriodSerializer(class_period)
        return Response(serializer.data)

    def put(self, request, id):
        class_period = ClassPeriod.objects.get(id=id)
        serializer = ClassPeriodSerializer(class_period, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        class_period = ClassPeriod.objects.get(id=id)
        class_period.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CourseListView(APIView):
    def get(self, request):
        serializer = MinimalCourseSerializer(Course.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CourseDetailView(APIView):
    def get(self, request, id):
        course = Course.objects.get(id=id)
        serializer = CourseSerializer(course)
        return Response(serializer.data)

    def put(self, request, id):
        course = Course.objects.get(id=id)
        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        course = Course.objects.get(id=id)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def post(self, request, id):
        course = Course.objects.get(id=id)
        action = request.data.get("action")
        if action == "assign_teacher":
            teacher_id = request.data.get("teacher")
            teacher = Teacher.objects.get(id=teacher_id)
            course.teachers.add(teacher)
            return Response({"status": "teacher assigned"}, status=status.HTTP_201_CREATED)
        return Response({"error": "Invalid action"}, status=status.HTTP_400_BAD_REQUEST)

class TeacherListView(APIView):
    def get(self, request):
        teachers = Teacher.objects.all()
        first_name = request.query_params.get("first_name")
        cv = request.query_params.get("cv")
        if first_name:
            students = students.filter(first_name=first_name)
        if cv:
            students = students.filter(cv=cv)
        serializer = MinimalTeacherSerializer(teachers, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TeacherDetailView(APIView):
    def get(self, request, id):
        teacher = Teacher.objects.get(id=id)
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data)

    def put(self, request, id):
        teacher = Teacher.objects.get(id=id)
        serializer = TeacherSerializer(teacher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        teacher = Teacher.objects.get(id=id)
        teacher.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class WeeklyTimetableView(APIView):
    def get(self, request):
        now = timezone.now()
        start_of_week = now - timedelta(days=now.weekday())
        end_of_week = start_of_week + timedelta(days=6)

        class_periods = ClassPeriod.objects.filter(
            start_time__gte=start_of_week,
            end_time__lte=end_of_week
        )

        timetable_data = {
            "start_of_week": start_of_week.isoformat(),
            "end_of_week": end_of_week.isoformat(),
            "class_periods": ClassPeriodSerializer(class_periods, many=True).data
        }
        return Response(timetable_data, status=status.HTTP_200_OK)

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
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        classroom = Classroom.objects.get(id=id)
        classroom.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def post(self, request, id):
        classroom = Classroom.objects.get(id=id)
        action = request.data.get("action")
        if action == "add_student":
            student_id = request.data.get("student")
            student = Student.objects.get(id=student_id)
            classroom.students.add(student)
            return Response({"status": "student added"}, status=status.HTTP_201_CREATED)
        return Response({"error": "Invalid action"}, status=status.HTTP_400_BAD_REQUEST)
