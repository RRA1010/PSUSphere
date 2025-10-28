from rest_framework import serializers
from studentorg.models import College, Student, Program

class CollegeSerializer(serializers.ModelSerializer):
  class Meta:
      model = College
      fields = [
         'college_name',
         'created_at',
         'updated_at',
      ]

class StudentSerializer(serializers.ModelSerializer):
   class Meta:
      model = Student
      fields = [
         'id',
         'student_id',
         'lastname',
         'firstname',
         'middlename',
         'program',
         'program_name'
      ]
      read_only_fields = ['program_name']

class ProgramSerializer(serializers.ModelSerializer):
   student = StudentSerializer(many=True, read_only=True, source='student_set')


   class Meta:
      model = Program
      fields = [
         'id',
         'prog_name',
         'college',
         'students',
      ]