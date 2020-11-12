from django.shortcuts import render

from .models import UserProfile, StudentClass, Student, Teacher, Course
from .serializers import UserProfileSerializer, StudentClassSerializer, StudentSerializer, TeacherSerializer, CourseSerializer

from rest_framework import viewsets

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class StudentClassViewSet(viewsets.ModelViewSet):
    queryset = StudentClass.objects.all()
    serializer_class = StudentClassSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
