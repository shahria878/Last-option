"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from . import settings
from django.conf.urls.static import static
from django.urls import path
from app1 import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentinfo/<str:id>/', views.StudentinfoPage, name='studentinfo'),
    path('',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('home/',views.HomePage,name='home'),
    path('alluser/',views.AllusersPage,name='alluser'),
    path('logout/',views.LogoutPage,name='logout'),
    path('changepass/',views.ChangepassPage,name='changepass'),
    path('result/<int:id>/', views.ResultPage, name='result'),
    path('result/<str:id>/', views.ResultPage, name='result'),
    path('result/',views.ResultPage, name='result'),
    path('admitcard/<int:id>/', views.admitcard_page, name='admitcard_page'),
    path('add-student/', views.create_student, name='add_student'),
    path('delete-student/<str:student_id>/', views.delete_student_confirm, name='delete_student'),
    path('register-courses/<int:id>/', views.course_register_page, name='register_courses'),
    path('admitform/', views.create_admitcard, name='admitform'),
    path('update-student/<int:student_id>/', views.update_student, name='update_student'),
    path('update-admitcard/<int:sid>/', views.update_admitcard, name='admitform'),
    path('resultform/', views.create_result, name='resultform'),
    path('update-result/<int:student_id>/', views.update_result, name='resultform'),
    path('total-result-form/', views.create_total_result, name='total_result_form'),
    path('results/', views.total_result_list, name='total_result_list'),
    path('total-result/update/<int:pk>/', views.update_total_result, name='update_total_result'),
    path('payment-details/<int:student_id>/', views.StudentPaymentPage, name='payment'),
    path('create-payment/', views.create_payment, name='paymentform'),
    path('payment-details/<str:studentid>/', views.StudentPaymentPage, name='student_payment'),
    path('payment/update/<int:payment_id>/', views.update_payment, name='paymentform'),
    path('update-payment/<int:student_id>/', views.update_payment, name='update_payment'),
    path('payment/update/<int:student_id>/', views.update_payment, name='update_payment'),
    path('payment/update/<int:sid>/', views.update_payment, name='update_payment'),
    path('update-payment/<int:sid>/', views.update_payment, name='update_payment'),
    






    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
