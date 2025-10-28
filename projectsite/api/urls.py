from django.urls import path
from . import views

urlpatterns = [
    #college
    path('colleges/', views.College_LC_APIView.as_view(), name='college-list-create'),
    path('colleges/<int:pk>/', views.College_RUD_APIView.as_view(), name='college-detail'),
    #program
    path('program/', views.Program_LC_APIView.as_view(), name='program-list-create'),
    path('program/<int:pk>/', views.Program_RUD_APIView.as_view(), name='program-detail'),
    #student
    path('student/', views.Student_LC_APIView.as_view(), name='student-list-create'),
    path('student/<int:pk>/',views.Student_RUD_APIView.as_view(), name='student-detail'),
]