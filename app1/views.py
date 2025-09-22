from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, get_object_or_404
from django.forms import modelformset_factory
from django.contrib.auth.forms import PasswordChangeForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.http import HttpResponse
from .forms import CourseRegisterFormSet
from django.db.models import Sum
from django.utils import timezone
from datetime import datetime
from .models import *
from .forms import *
# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    return render (request,'home.html')

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
        



    return render (request,'signup.html')

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

    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')

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
            return redirect('logout')  # Or wherever you want to redirect
        
    students = Student.objects.all()
    infos = StudentInfo.objects.all()
    context = {'students': students,
               'infos': infos}
    return render(request, 'changepass.html',context=context)





def notification_list(request):
    notifications = Notification.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'notifications.html', {'notifications': notifications})

def StudentinfoPage(request, id):
    students = get_object_or_404(StudentProfile, pk=id)
    infos = StudentInfo.objects.filter(pk=id)
    context = {
        'students': students,
        'infos': infos
    }
    return render(request, 'studentinfo.html', context)


def course_register_page(request, id):
    student = get_object_or_404(Student, pk=id)
    infos = StudentInfo.objects.filter(sroll=student)
    registers = CourseRegister.objects.filter(studentid=student)

    context = {
        'student': student,
        'infos': infos,
        'registers': registers
    }

    return render(request, 'course_register.html', context=context)




def AllusersPage(request):
    students = Student.objects.all()
    infos = StudentInfo.objects.all()
    context = {'students': students,
               'infos': infos}
    return render(request, 'alluser.html',context=context)





def StudentPaymentPage(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    infos = StudentInfo.objects.filter(sroll=student)
    admitcards = FinalAdmitCard.objects.filter(fid=student)
    registers = CourseRegister.objects.filter(studentid=student)
    payments = LastPayment.objects.filter(l_student=student)

    today = timezone.now().date()

    context = {
        'student': student,
        'infos': infos,
        'admitcards': admitcards,
        'registers': registers,
        'payments': payments,
        'today': today,
    }
    return render(request, 'payment.html', context)

def admitcard_page(request, id):
    student = get_object_or_404(Student, pk=id)
    infos = StudentInfo.objects.filter(sroll=student)
    admitcards = FinalAdmitCard.objects.filter(fid=student)
    registers = CourseRegister.objects.filter(studentid=student)
    payments = LastPayment.objects.filter(l_student=student)

    has_paid = all(p.l_status == "Paid" for p in payments)

    total_credits = sum([reg.credits for reg in registers])

    context = {
        'student': student,
        'infos': infos,
        'admitcards': admitcards,
        'registers': registers,
        'payments': payments,
        'has_paid': has_paid,
        'total_credits': total_credits,
        'today': datetime.now(),
    }

    return render(request, 'admitcard_page.html', context)




def ResultPage(request, id):
    student = get_object_or_404(Student, pk=id)
    infos = StudentInfo.objects.filter(sroll=student)
    admitcards = FinalAdmitCard.objects.filter(fid=student)
    registers = CourseRegister.objects.filter(studentid=student)
    results = Result.objects.filter(mainid=student)
    tresults = TotalResult.objects.filter(r_id=student)

    context = {
        'student': student,
        'infos': infos,
        'admitcards': admitcards,
        'registers': registers,
        'results': results,
        'tresults': tresults,
    }
    return render (request,'result.html',context=context)

def total_result_list(request):
    return render(request, 'results.html')




@csrf_exempt
def create_student(request):
    if request.method == 'POST':
        student_form = StudentForm(request.POST)
        profile_form = StudentProfileForm(request.POST)
        info_form = StudentInfoForm(request.POST, request.FILES)

        CourseRegisterFormSetCreate = modelformset_factory(
            CourseRegister,
            form=CourseRegisterForm,
            extra=2,  # always 2 forms for new student
            can_delete=False
        )
        course_formset = CourseRegisterFormSetCreate(request.POST, queryset=CourseRegister.objects.none())


        if (student_form.is_valid() and profile_form.is_valid() and 
            info_form.is_valid() and course_formset.is_valid()):
            
            student = student_form.save()

            profile = profile_form.save(commit=False)
            profile.roll = student
            profile.save()

            info = info_form.save(commit=False)
            info.sroll = student
            info.save()

            courses = course_formset.save(commit=False)
            for course in courses:
                course.studentid = student
                course.save()

            return redirect('paymentform')
    
    else:
        student_form = StudentForm()
        profile_form = StudentProfileForm()
        info_form = StudentInfoForm()

        CourseRegisterFormSetCreate = modelformset_factory(
            CourseRegister,
            form=CourseRegisterForm,
            extra=2,
            can_delete=False
        )
        course_formset = CourseRegisterFormSetCreate(queryset=CourseRegister.objects.none())


    context = {
        'student_form': student_form,
        'profile_form': profile_form,
        'info_form': info_form,
        'course_formset': course_formset,
        'update': False,
    }
    return render(request, 'student_form.html', context)

@csrf_exempt
def create_payment(request):
    if request.method == 'POST':
        form = LastPaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admitform')  # Replace with your actual success page/view
    else:
        form = LastPaymentForm()

    return render(request, 'paymentform.html', {'form': form})
    



@csrf_exempt
def create_admitcard(request):
    if request.method == 'POST':
        form = FinalAdmitCardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('resultform')  # Redirect to the desired page after successful submission
    else:
        form = FinalAdmitCardForm()

    context = {
        'admitcard_form': form,
    }
    return render(request, 'admitform.html', context)
@csrf_exempt
def create_result(request):
    ResultFormsetCreate = modelformset_factory(
        Result,
        form=ResultForm,
        extra=2,  # Change as needed
        can_delete=False
    )

    if request.method == 'POST':
        result_formset = ResultFormsetCreate(request.POST, queryset=Result.objects.none())

        if result_formset.is_valid():
            result_formset.save()
            return redirect('total_result_form')  # Replace with actual URL name or redirect
    else:
        result_formset = ResultFormsetCreate(queryset=Result.objects.none())

    context = {
        'result_formset': result_formset,
        'update': False,
    }
    return render(request, 'resultform.html', context)


@csrf_exempt
def create_total_result(request):
    if request.method == 'POST':
        form = TotalResultForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('alluser')  # Change to your desired redirect URL
    else:
        form = TotalResultForm()
    return render(request, 'total_result_form.html', {'form': form})





@csrf_exempt
def update_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    profile = get_object_or_404(StudentProfile, roll=student)
    info = get_object_or_404(StudentInfo, sroll=student)

    course_registers = CourseRegister.objects.filter(studentid=student)
    CourseRegisterFormSetUpdate = modelformset_factory(
        CourseRegister,
        form=CourseRegisterForm,
        extra=0,
        can_delete=True
    )

    if request.method == 'POST':

        print(request.POST)
        student_form = StudentForm(request.POST, instance=student)
        profile_form = StudentProfileForm(request.POST, instance=profile)
        info_form = StudentInfoForm(request.POST, request.FILES, instance=info)
        course_formset = CourseRegisterFormSetUpdate(request.POST, queryset=course_registers)

        if (student_form.is_valid() and profile_form.is_valid() and 
            info_form.is_valid() and course_formset.is_valid()):
            
            student = student_form.save()

            profile = profile_form.save(commit=False)
            profile.roll = student
            profile.save()

            info = info_form.save(commit=False)
            info.sroll = student
            info.save()

            courses = course_formset.save(commit=False)
            for course in courses:
                course.studentid = student
                course.save()

            for course in course_formset.deleted_objects:
                course.delete()

            return redirect('admitform', sid=student.id)
        
    else:
        
        student_form = StudentForm(instance=student)
        profile_form = StudentProfileForm(instance=profile)
        info_form = StudentInfoForm(instance=info)
        course_formset = CourseRegisterFormSetUpdate(queryset=course_registers)

    context = {
        'student_form': student_form,
        'profile_form': profile_form,
        'info_form': info_form,
        'course_formset': course_formset,
        'update': True,
        'student_id': student.id,
    }
    return render(request, 'student_form.html', context)


@csrf_exempt
def update_payment(request, pk):

    student = get_object_or_404(Student, id=pk)
    payment= LastPaymentForm.objects.filter(l_student=student).first()

    if request.method == 'POST':
        form = LastPaymentForm(request.POST, instance=payment)
        if form.is_valid():
            form.save()
            return redirect('payment_list')  
    else:
        form = LastPaymentForm(instance=payment)
    return render(request, 'payment_form.html', {'form': form})


@csrf_exempt
def update_admitcard(request, sid):
    student = get_object_or_404(Student, id=sid)
    admitcard = FinalAdmitCard.objects.filter(fid=student).first()

    if request.method == 'POST':
        admitcard_form = FinalAdmitCardForm(request.POST, instance=admitcard)
        if admitcard_form.is_valid():
            admitcard_form.save()
            return redirect('paymentform') 
    else:
        admitcard_form = FinalAdmitCardForm(instance=admitcard)

    context = {
        'admitcard_form': admitcard_form,
    }
    return render(request, 'admitform.html', context)


@csrf_exempt
def update_result(request, student_id):
    student = get_object_or_404(Student, pk=student_id)

    queryset = Result.objects.filter(mainid=student)

    ResultFormsetUpdate = modelformset_factory(Result, form=ResultForm, extra=0)

    if request.method == 'POST':
        formset = ResultFormsetUpdate(request.POST, queryset=queryset)
        if formset.is_valid():
            instances = formset.save(commit=False)
            for instance in instances:
                instance.mainid = student  
                instance.save()
            return redirect('result', id=student_id)
    else:
        formset = ResultFormsetUpdate(queryset=queryset)

    context = {
        'student': student,
        'result_formset': formset,
    }
    return render(request, 'resultform.html', context)

# Update View
def update_total_result(request, pk):

    student = get_object_or_404(Student, id=pk)
    result = TotalResultForm.objects.filter(r_id=student).first()

    
    if request.method == 'POST':
        form = TotalResultForm(request.POST, instance=result)
        if form.is_valid():
            form.save()
            return redirect('alluser')  # Change to your desired redirect URL
    else:
        form = TotalResultForm(instance=result)

    context = {
        'form': form,
    }
    return render(request, 'total_result_form.html', context)


@login_required
def delete_student_confirm(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    if request.method == 'POST':
        # Delete related records
        StudentProfile.objects.filter(roll=student).delete()
        StudentInfo.objects.filter(sroll=student).delete()
        CourseRegister.objects.filter(studentid=student).delete()
        LastPayment.objects.filter(l_student=student).delete()
        FinalAdmitCard.objects.filter(fid=student).delete()

        # Delete the student record
        student.delete()

        return redirect('alluser')  # Your URL name for student list page

    return render(request, 'delete_confirm.html', {'student': student})



