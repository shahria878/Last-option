from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Student(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    

    def __str__(self):
        return self.id
    
class StudentProfile(models.Model):
    roll = models.ForeignKey(Student, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class StudentInfo(models.Model):
    sroll = models.ForeignKey(Student, on_delete=models.CASCADE)
    sname = models.CharField(max_length=100)
    fathername = models.CharField(max_length=100)
    mothername = models.CharField(max_length=100)
    program = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    guardianphone = models.CharField(max_length=100)
    session = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    dob = models.CharField(max_length=100)
    email = models.EmailField()
    pic = models.ImageField(upload_to='student_pics/', null=True, blank=True)

    def __str__(self):
        return f"{self.sname} ({self.sroll})"
    

class CourseRegister(models.Model):
    studentid = models.ForeignKey(Student, on_delete=models.CASCADE)
    code = models.CharField(max_length=10, null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    credits = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    semester = models.CharField(max_length=10, null=True, blank=True)
    type = models.CharField(max_length=10, null=True, blank=True)
    section = models.CharField(
        max_length=20,
        choices=[('Remove', 'Remove'), ('Add', 'Add')]
    )
    section_name_time = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.code} - {self.title}"
    

class AdmitCard(models.Model):
    sid = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='admitcard_student')
    schedule = models.CharField(max_length=100, null=True, blank=True)
    exam = models.CharField(
        max_length=20,
        choices=[('Mid', 'Mid'), ('Final', 'Final')]
    )
    bill = models.CharField(
        max_length=20,
        choices=[('Paid', 'Paid'), ('Prepaid', 'Prepaid'), ('Unpaid', 'Unpaid'), ('Halfpaid', 'Halfpaid')]
    )


class Result(models.Model):
    mainid = models.ForeignKey(Student, on_delete=models.CASCADE)
    s_code = models.ForeignKey(CourseRegister, on_delete=models.CASCADE, related_name='results_by_code')
    s_title = models.ForeignKey(CourseRegister, on_delete=models.CASCADE, related_name='results_by_title')
    grade = models.CharField(max_length=10, null=True, blank=True)
    grade_point = models.CharField(max_length=10, null=True, blank=True)
    cur_status = models.CharField(max_length=10, null=True, blank=True)

    

