from django.urls import path
from . import views

urlpatterns = [
    # Degree Program
    path('degree-programs/', views.DegreeProgramList.as_view(), name='degree-program-list'),
    path('degree-programs/<int:pk>/', views.DegreeProgramDetail.as_view(), name='degree-program-detail'),

    # Degree Name
    path('degrees/', views.DegreeNameList.as_view(), name='degree-name-list'),
    path('degrees/<str:pk>/', views.DegreeNameDetail.as_view(), name='degree-name-detail'),

    # Departments
    path('departments/', views.DepartmentList.as_view(), name='department-list'),
    path('departments/<int:pk>/', views.DepartmentDetail.as_view(), name='department-detail'),

    # Courses
    path('courses/', views.CourseList.as_view(), name='course-list'),
    path('courses/<int:pk>/', views.CourseDetail.as_view(), name='course-detail'),

    # Semesters
    path('semesters/', views.SemesterList.as_view(), name='semester-list'),
    path('semesters/<int:pk>/', views.SemesterDetail.as_view(), name='semester-detail'),

      # Subjects
    path('subjects/', views.SubjectList.as_view(), name='subject-list'),
    path('subjects/<int:pk>/', views.SubjectDetail.as_view(), name='subject-detail'),
]
