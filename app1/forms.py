from django import forms
from .models import Student, StudentProfile, StudentInfo, CourseRegister, AdmitCard
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

class AdmitCardForm(forms.ModelForm):
    class Meta:
        model = AdmitCard
        fields = [
            'sid',
            'prog',
            'sess',
            'seme',
            'cou_code',
            'tit',
            'cre',
            'schedule',
            'exam',
            'bill',
        ]


