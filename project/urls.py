from django.contrib import admin
from . import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path
from app1 import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('home/',views.HomePage,name='home'),
    path('logout/',views.LogoutPage,name='logout'),

    path('studentinfo/<str:id>/', views.StudentinfoPage, name='studentinfo'),
    path('alluser/',views.AllusersPage,name='alluser'),
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
    path('payment/update/<int:student_id>/', views.update_payment, name='paymentform'),
    path('update-payment/<int:student_id>/', views.update_payment, name='update_payment'),
    path('payment/update/<int:student_id>/', views.update_payment, name='update_payment'),
    path('payment/update/<int:sid>/', views.update_payment, name='update_payment'),
    path('update-payment/<int:sid>/', views.update_payment, name='update_payment'),
    path('notifications/', views.notification_list, name='notification_list'),
    
    






    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)