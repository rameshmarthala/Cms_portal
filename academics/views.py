from rest_framework import generics
from .models import Degree_Program, Degree_name, Departments, Course, Semesters,Subject
from .serializers import (
    DegreeProgramSerializer, DegreeNameSerializer, DepartmentSerializer,
    CourseSerializer, SemesterSerializer , SubjectSerializer
)

# -------------------------------
# Degree Program Views
# -------------------------------
class DegreeProgramList(generics.ListCreateAPIView):
    queryset = Degree_Program.objects.all()
    serializer_class = DegreeProgramSerializer

class DegreeProgramDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Degree_Program.objects.all()
    serializer_class = DegreeProgramSerializer

# -------------------------------
# Degree Name Views
# -------------------------------
class DegreeNameList(generics.ListCreateAPIView):
    queryset = Degree_name.objects.all()
    serializer_class = DegreeNameSerializer

class DegreeNameDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Degree_name.objects.all()
    serializer_class = DegreeNameSerializer

# -------------------------------
# Department Views
# -------------------------------
class DepartmentList(generics.ListCreateAPIView):
    queryset = Departments.objects.all()
    serializer_class = DepartmentSerializer

class DepartmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Departments.objects.all()
    serializer_class = DepartmentSerializer

# -------------------------------
# Course Views
# -------------------------------
class CourseList(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

# -------------------------------
# Semester Views
# -------------------------------
class SemesterList(generics.ListCreateAPIView):
    queryset = Semesters.objects.all()
    serializer_class = SemesterSerializer

class SemesterDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Semesters.objects.all()
    serializer_class = SemesterSerializer


# -------------------------------
# Subject Views
# -------------------------------
class SubjectList(generics.ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class SubjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer