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
    

class StudentPayment(models.Model):
    s_student = models.ForeignKey(Student, on_delete=models.CASCADE)
    s_waiver = models.CharField(max_length=100, null=True, blank=True)
    s_due_date = models.DateField()
    s_payment_type = models.CharField(
        max_length=50,
        choices=[
            ('Tuition(mid)', 'Tuition(mid)'),
            ('Admission', 'Admission'),
            ('Registration', 'Registration'),
            ('Late Fee', 'Late Fee'),
            ('Retake Fee', 'Retake Fee'),
            ('Other', 'Other'),
        ]
    )
    s_total_bill = models.DecimalField(max_digits=10, decimal_places=2)
    s_total_paid = models.DecimalField(max_digits=10, decimal_places=2)
    s_due = models.DecimalField(max_digits=10, decimal_places=2)
    s_payment_date = models.DateField()
    s_transaction_id = models.CharField(max_length=100, unique=True)
    s_STATUS_CHOICES = [
        ('Paid', 'Paid'),
        ('UnPaid', 'UnPaid'),
    ]
    s_status = models.CharField(max_length=10, choices=s_STATUS_CHOICES)
    s_remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.s_student} - {self.s_payment_type} - {self.s_due} BDT"
    

class Payment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    waiver = models.CharField(max_length=100, null=True, blank=True)
    payment_type = models.CharField(
        max_length=50,
        choices=[
            ('Tuition(mid)', 'Tuition(mid)'),
            ('Admission', 'Admission'),
            ('Registration', 'Registration'),
            ('Late Fee', 'Late Fee'),
            ('Retake Fee', 'Retake Fee'),
            ('Other', 'Other'),
        ]
    )
    total_bill = models.DecimalField(max_digits=10, decimal_places=2)
    total_paid = models.DecimalField(max_digits=10, decimal_places=2)
    due = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.CharField(max_length=10, null=True, blank=True)
    transaction_id = models.CharField(max_length=100, unique=True)
    status = models.CharField(
        max_length=20,
        choices=[('Pending', 'Pending'), ('Completed', 'Completed'), ('Failed', 'Failed')],
        default='Completed'
    )
    remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.student} - {self.payment_type} - {self.due} BDT"

    

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

    def __str__(self):
        return f"{self.s_code} - {self.grade}"
    
class TotalResult(models.Model):
    r_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    batch = models.CharField(max_length=20, null=True, blank=True)
    total_att_credit = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    total_earn_credit = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    gpa = models.CharField(max_length=20, null=True, blank=True)
    cgpa = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f"{self.r_id} - {self.cgpa}"




    

