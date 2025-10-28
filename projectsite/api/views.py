from django.shortcuts import render
from studentorg.models import College, Program, Student
from .serializer import CollegeSerializer, ProgramSerializer, StudentSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny

# Create your views here.

#List all or create new colleges (protected)
class College_LC_APIView(generics.ListCreateAPIView):
    queryset = College.objects.all()
    serializer_class = CollegeSerializer
    permission_classes = [IsAuthenticated]

# Retrieve, update, or delete a single college (protected)
class College_RUD_APIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = College.objects.all()
    serializer_class = CollegeSerializer
    permission_classes = [IsAuthenticated]

class Program_LC_APIView(generics.ListCreateAPIView):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer
    permission_classes = [IsAuthenticated]

class Program_RUD_APIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer
    permission_classes = [IsAuthenticated]

class Student_LC_APIView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]

class Student_RUD_APIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]
    



