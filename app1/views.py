from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from .forms import CourseRegisterFormSet
from .models import *
from .forms import *
# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    return render(request, 'home.html')

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')


        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
    
    return render(request, 'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render(request, 'login.html')

login_required
def ChangepassPage(request):
    if request.method == 'POST':
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            return HttpResponse("Passwords do not match!")
        else:
            user = request.user
            user.set_password(pass1)  # Proper way to change password
            user.save()
            update_session_auth_hash(request, user)  # Keeps user logged in
            return redirect('login')  # Or wherever you want to redirect
        
    students = Student.objects.all()
    infos = StudentInfo.objects.all()
    context = {'students': students,
               'infos': infos}
    return render(request, 'changepass.html',context=context)

def StudentinfoPage(request, id):
    students = get_object_or_404(StudentProfile, pk=id)
    infos = StudentInfo.objects.filter(pk=id)
    context = {
        'students': students,
        'infos': infos
    }
    return render(request, 'studentinfo.html', context)


def AllusersPage(request):
    students = Student.objects.all()
    infos = StudentInfo.objects.all()
    context = {'students': students,
               'infos': infos}
    return render(request, 'alluser.html',context=context)


def LogoutPage(request):
    logout(request)
    return redirect('login')

def AdmitcardPage(request):
    students = Student.objects.all()
    registers = CourseRegister.objects.all()
    context = {'registers': registers, 
               'students': students}
    return render (request,'admitcard.html',context=context)


def CourseregisterPage(request):
    registers = CourseRegister.objects.all()
    students = Student.objects.all()
    context = {'registers': registers, 
               'students': students}
    return render(request, 'courseregister.html',context=context)


def ResultPage(request):
    students = Student.objects.all()
    context = {'students': students}
    return render (request,'result.html',context=context)

def create_student(request):
    if request.method == 'POST':
        student_form = StudentForm(request.POST)
        profile_form = StudentProfileForm(request.POST)
        info_form = StudentInfoForm(request.POST, request.FILES)

        if student_form.is_valid() and profile_form.is_valid() and info_form.is_valid():
            student = student_form.save()

            profile = profile_form.save(commit=False)
            profile.roll = student
            profile.save()

            info = info_form.save(commit=False)
            info.sroll = student
            info.save()

            return redirect('alluser')  # Redirect to a success page or student list

    else:
        student_form = StudentForm()
        profile_form = StudentProfileForm()
        info_form = StudentInfoForm()

    context = {
        'student_form': student_form,
        'profile_form': profile_form,
        'info_form': info_form
    }

    return render(request, 'student_form.html', context)

def update_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    profile = get_object_or_404(StudentProfile, roll=student)
    info = get_object_or_404(StudentInfo, sroll=student)

    if request.method == 'POST':
        student_form = StudentForm(request.POST, instance=student)
        profile_form = StudentProfileForm(request.POST, instance=profile)
        info_form = StudentInfoForm(request.POST, request.FILES, instance=info)

        if student_form.is_valid() and profile_form.is_valid() and info_form.is_valid():
            student_form.save()

            profile = profile_form.save(commit=False)
            profile.roll = student
            profile.save()

            info = info_form.save(commit=False)
            info.sroll = student
            info.save()

            return redirect('alluser')  # Or redirect to a detail page

    else:
        student_form = StudentForm(instance=student)
        profile_form = StudentProfileForm(instance=profile)
        info_form = StudentInfoForm(instance=info)

    context = {
        'student_form': student_form,
        'profile_form': profile_form,
        'info_form': info_form,
        'update': True,
        'student_id': student.id,
    }

    return render(request, 'student_form.html', context)

def delete_student_confirm(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    if request.method == 'POST':
        student.delete()
        return redirect('alluser')  # Replace with your actual list view name

    return render(request, 'delete_confirm.html', {'student': student})



def register_courses(request, id):
    students = get_object_or_404(Student, pk = id)

    if request.method == 'POST':
        formset = CourseRegisterFormSet(request.POST, queryset=CourseRegister.objects.none())
        if formset.is_valid():
            instances = formset.save(commit=False)
            for instance in instances:
                instance.studentid = students  # Assign the same student
                instance.save()
            return redirect('studentinfo')  # Change this to your success URL
    else:
        formset = CourseRegisterFormSet(queryset=CourseRegister.objects.none())

    return render(request, 'register_courses.html', {'formset': formset, 'students': students})






    
