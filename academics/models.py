from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# -------------------------------
# Degree Program
# -------------------------------
class Degree_Program(models.Model):
    degree_Program = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f'{self.degree_Program}'


# -------------------------------
# Degree Name
# -------------------------------
class Degree_name(models.Model):
    degree_program = models.ForeignKey(Degree_Program, on_delete=models.CASCADE, related_name='degree_name')
    degree_name = models.CharField(
        max_length=100, blank=False, primary_key=True,
        help_text='Enter Degree Name like B.Tech, B.Sc..etc'
    )
    degree_duration = models.IntegerField(choices=[(i, f"{i} Years") for i in range(1, 10)])
    degree_code = models.CharField(unique=True, max_length=10)

    def __str__(self):
        return f'{self.degree_name} ({self.degree_duration} Years, {self.degree_code}, {self.degree_program})'


# -------------------------------
# Departments
# -------------------------------
class Departments(models.Model):
    degree_name = models.ForeignKey(Degree_name, on_delete=models.CASCADE)
    department_name = models.CharField(max_length=100, help_text='Enter Department Name like CSE, ECE, EEE..etc')

    class Meta:
        unique_together = ('degree_name', 'department_name')

    def __str__(self):
        return f'{self.department_name} ({self.degree_name})'


# -------------------------------
# Courses
# -------------------------------
class Course(models.Model):
    degree_name = models.ForeignKey(Degree_name, on_delete=models.CASCADE, related_name='course_name')
    department_name = models.ForeignKey(Departments, on_delete=models.CASCADE, related_name='courses')
    course_name = models.CharField(max_length=100, help_text='Enter Course Name like Computer Science Engineering..etc')
    course_fee = models.CharField(max_length=15, help_text='Enter fee per Year')
    course_code = models.CharField(max_length=20, help_text='Enter Course Code Here..')

    def save(self, *args, **kwargs):
        # Ensure course_fee is stored as integer string
        if self.course_fee:
            self.course_fee = str(int(float(self.course_fee)))
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.course_name} (Fee: {self.course_fee}, Code: {self.course_code})'


# -------------------------------
# Semesters
# -------------------------------
class Semesters(models.Model):
    course_name = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='semesters')
    semester_number = models.IntegerField(help_text='Enter which semester it is')

    class Meta:
        unique_together = ('course_name', 'semester_number')

    def __str__(self):
        return f'Semester {self.semester_number} - {self.course_name}'

# -------------------------------
# Subject Model
# -------------------------------

class Subject(models.Model):
    subject_name = models.CharField(max_length=100, help_text="Enter Subject Name")
    subject_code = models.CharField(max_length=20, help_text="Enter Unique Subject Code")
    credits = models.IntegerField(help_text="Enter Credits for the Subject")

    semester = models.ForeignKey(Semesters, on_delete=models.CASCADE, related_name='subjects')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='subjects')

    class Meta:
        unique_together = ('semester', 'subject_code')  # ensures unique code per semester

    def __str__(self):
        return f'{self.subject_name} ({self.subject_code}) - Sem {self.semester.semester_number}'

# -------------------------------
# Auto-create semesters after a course is created
# -------------------------------
@receiver(post_save, sender=Course)
def create_semesters_for_course(sender, instance, created, **kwargs):
    if created:
        total_semesters = instance.degree_name.degree_duration * 2  # Assuming 2 semesters per year
        for i in range(1, total_semesters + 1):
            Semesters.objects.create(course_name=instance, semester_number=i)
