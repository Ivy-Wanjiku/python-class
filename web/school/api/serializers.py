from rest_framework import serializers
from classperiod.models import ClassPeriod
from classroom.models import Classroom
from course.models import Course
from student.models import Student
from teacher.models import Teacher



class MinimalTeacherSerializer(serializers.ModelSerializer):
    full_name=serializers.SerializerMethodField()
    def get_full_name(self,object):
        return f"{object.first_name} {object.last_name}"
    class Meta:
        model=Teacher
        fields=["id","full_name","email","cv","unit_taught"]

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model =Teacher
        fields = "__all__"

class MinimalCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields=["id","title","course_code","number_of_topics","duration"]

class MinimalStudentSerializer(serializers.ModelSerializer):
    full_name=serializers.SerializerMethodField()
    def get_full_name(self,object):
        return f"{object.first_name} {object.last_name}"
    class Meta:
        model=Student
        fields=["id","full_name","email"]

class CourseSerializer(serializers.ModelSerializer):
    teachers = TeacherSerializer(many=True)
    class Meta:
        model =Course
        fields = "__all__"

class StudentSerializer(serializers.ModelSerializer):
    coursename=CourseSerializer(many=True)
    class Meta:
        model =Student
        fields= "__all__"
class MinimalClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model=Classroom
        fields=["id","class_name","class_num"]
class ClassroomSerializer(serializers.ModelSerializer):
    students = MinimalStudentSerializer(many=True)
    teacher=TeacherSerializer(many=True)
    class Meta:
        model =Classroom
        fields = "__all__"
class MinimalClassPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model=ClassPeriod
        fields=["id","start_time","end_time"]
class ClassPeriodSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer()
    course = CourseSerializer()
    class Meta:
        model =ClassPeriod
        fields = "__all__"
