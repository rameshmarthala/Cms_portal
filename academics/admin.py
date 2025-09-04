from django.contrib import admin
from .models import Degree_Program, Degree_name, Departments, Course, Semesters,Subject

# -------------------------------
# Admin for Degree Program
# -------------------------------
@admin.register(Degree_Program)
class DegreeProgramAdmin(admin.ModelAdmin):
    list_display = ('id', 'degree_Program')
    search_fields = ('degree_Program',)

# -------------------------------
# Admin for Degree Name
# -------------------------------
@admin.register(Degree_name)
class DegreeNameAdmin(admin.ModelAdmin):
    list_display = ('degree_name', 'degree_duration', 'degree_code', 'degree_program')
    search_fields = ('degree_name', 'degree_code')

# -------------------------------
# Admin for Departments
# -------------------------------
@admin.register(Departments)
class DepartmentsAdmin(admin.ModelAdmin):
    list_display = ('department_name', 'degree_name')
    search_fields = ('department_name',)
    list_filter = ('degree_name',)

# -------------------------------
# Admin for Course
# -------------------------------
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'course_code', 'course_fee', 'degree_name', 'department_name')
    search_fields = ('course_name', 'course_code')
    list_filter = ('degree_name', 'department_name')

# -------------------------------
# Admin for Semesters
# -------------------------------
@admin.register(Semesters)
class SemesterAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'semester_number')
    search_fields = ('course_name__course_name',)
    list_filter = ('course_name',)


# -------------------------------
# Subject Admin
# -------------------------------
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('subject_name', 'subject_code', 'credits', 'semester', 'course')
    search_fields = ('subject_name', 'subject_code')
    list_filter = ('semester', 'course')
