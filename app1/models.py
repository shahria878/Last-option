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
    
class LastPayment(models.Model):
    l_student = models.ForeignKey(Student, on_delete=models.CASCADE)
    l_waiver_persent = models.CharField(max_length=100, null=True, blank=True)
    l_due_date = models.DateField()
    l_fee_type = models.CharField(
        max_length=200,
        choices=[
            ('1st Installment Registration', '1st Installment Registration'),
            ('2nd Installment 30% of the Tuition Fees', '2nd Installment 30% of the Tuition Fees'),
            ('3rd Installment 30% of the Tuition Fee(Mid term)', '3rd Installment 30% of the Tuition Fee(Mid term)'),
            ('4th Installment 40% of the Tuition Fee(Final)', '4th Installment 40% of the Tuition Fee(Final)'),
            ('Late Fees', 'Late Fees'),
        ]
    )
    l_fees = models.DecimalField(max_digits=10, decimal_places=2)
    l_payment_type = models.CharField(
        max_length=100,
        choices=[
            ('Tuition(Mid Term)', 'Tuition(Mid Term)'),
            ('Tuition(Final)', 'Tuition(Final)'),
            ('Student Payment', 'Student Payment'),
            ('Registration', 'Registration'),
            ('Late Fees', 'Late Fees'),
            ('Repeat Exam Fee', 'Repeat Exam Fee'),
            ('Additional Waiver', 'Additional Waiver'),
            ('Caution money', 'Caution money'),
            ('Admission and varificatin fees', 'Admission and varificatin fees'),
            ('Other', 'Other'),

        ]
    )
    l_waiver_taka = models.DecimalField(max_digits=10, decimal_places=2)
    l_installment = models.DecimalField(max_digits=10, decimal_places=2)
    l_pay = models.DecimalField(max_digits=10, decimal_places=2)
    l_total_bill = models.DecimalField(max_digits=10, decimal_places=2)
    l_total_paid = models.DecimalField(max_digits=10, decimal_places=2)
    l_due = models.DecimalField(max_digits=10, decimal_places=2)
    l_payment_date = models.DateField(null=True, blank=True)
    l_transaction_id = models.CharField(max_length=100, unique=True)
    l_STATUS_CHOICES = [
        ('Paid', 'Paid'),
        ('UnPaid', 'UnPaid'),
    ]
    l_status = models.CharField(max_length=10, choices=l_STATUS_CHOICES)
    l_remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.l_student} - {self.l_payment_type} - {self.l_due} BDT"
    
    

class FinalAdmitCard(models.Model):
    fid = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='admit_student')
    fsemester = models.ForeignKey(StudentInfo, on_delete=models.CASCADE, related_name='admit_semester')
    fbill = models.ForeignKey(LastPayment, on_delete=models.CASCADE, related_name='admitcard_bill')
    fexam = models.CharField(
        max_length=20,
        choices=[('Mid', 'Mid'), ('Final', 'Final')]
    )
    fschedule = models.CharField(max_length=100, null=True, blank=True)

    


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
    


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"To {self.user.username}: {self.message[:20]}"




    

