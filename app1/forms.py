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

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = [
            'student',
            'waiver',
            'payment_type',
            'total_bill',
            'total_paid',
            'due',
	        'payment_date',
            'transaction_id',
            'status',
            'remarks',
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