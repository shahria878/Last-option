from django.forms import ModelForm
from django.forms import modelformset_factory
from .models import *

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['id']

class StudentProfileForm(ModelForm):
    class Meta:
        model = StudentProfile
        fields = ['name']

class StudentInfoForm(ModelForm):
    class Meta:
        model = StudentInfo
        fields = ['sname', 'fathername', 'mothername', 'program', 'gender', 'phone',
                  'guardianphone', 'session', 'nationality', 'dob', 'email', 'pic']
        


class CourseRegisterForm(ModelForm):
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
    extra=5  # 3 empty rows initially, you can change this number
)