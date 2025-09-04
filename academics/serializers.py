from rest_framework import serializers
from .models import Degree_Program, Degree_name, Departments, Course, Semesters,Subject

# -------------------------------
# Degree Program Serializer
# -------------------------------
class DegreeProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Degree_Program
        fields = '__all__'

# -------------------------------
# Degree Name Serializer
# -------------------------------
class DegreeNameSerializer(serializers.ModelSerializer):
    degree_program = DegreeProgramSerializer(read_only=True)
    
    class Meta:
        model = Degree_name
        fields = '__all__'

# -------------------------------
# Department Serializer
# -------------------------------
class DepartmentSerializer(serializers.ModelSerializer):
    degree_name = DegreeNameSerializer(read_only=True)

    class Meta:
        model = Departments
        fields = '__all__'

# -------------------------------
# Course Serializer
# -------------------------------
class CourseSerializer(serializers.ModelSerializer):
    degree_name = DegreeNameSerializer(read_only=True)
    department_name = DepartmentSerializer(read_only=True)
    
    class Meta:
        model = Course
        fields = '__all__'

# -------------------------------
# Semester Serializer
# -------------------------------
class SemesterSerializer(serializers.ModelSerializer):
    course_name = CourseSerializer(read_only=True)

    class Meta:
        model = Semesters
        fields = '__all__'

# -------------------------------
# Subject Serializer
# -------------------------------
class SubjectSerializer(serializers.ModelSerializer):
    semester = serializers.StringRelatedField(read_only=True)
    course = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Subject
        fields = '__all__'