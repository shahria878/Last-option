from django import forms
from .models import *
from django.forms import modelformset_factory

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['id']

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ['name']

class StudentInfoForm(forms.ModelForm):
    class Meta:
        model = StudentInfo
        fields = ['sname', 'fathername', 'mothername', 'program', 'gender', 'phone',
                  'guardianphone', 'session', 'nationality', 'dob', 'email', 'pic']
        

class CourseRegisterForm(forms.ModelForm):
    class Meta:
        model = CourseRegister
        fields = [
            'code',
            'title',
            'credits',
            'semester',
            'type',
            'section',
            'section_name_time',
        ]

CourseRegisterFormSet = modelformset_factory(
    CourseRegister,
    form=CourseRegisterForm,
    extra=2  # you can change this
)

class TotalPaymentForm(forms.ModelForm):
    class Meta:
        model = TotalPayment
        fields = [
            't_student',
            't_waiver',
            't_due_date',
            't_payment_type',
            'installment',
            'pay',
            't_total_bill',
            't_total_paid',
            't_due',
	        't_payment_date',
            't_transaction_id',
            't_status',
            't_remarks',
        ]


class AdmitCardForm(forms.ModelForm):
    class Meta:
        model = AdmitCard
        fields = [
            'sid',
            'schedule',
            'exam',
            'bill',
        ]

class ResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = [
            'mainid',
            's_code',
            's_title',
            'grade',
            'grade_point',
            'cur_status',
        ]

ResultFormset = modelformset_factory(
        Result,
        form=ResultForm,
        extra=2  # Change as needed
)


class TotalResultForm(forms.ModelForm):
    class Meta:
        model = TotalResult
        fields = [
            'r_id',
            'batch',
            'total_att_credit',
            'total_earn_credit',
            'gpa',
            'cgpa',
        ]