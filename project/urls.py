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
    path('result/',views.ResultPage, name='result'),
    path('admitcard/<int:id>/', views.admitcard_page, name='admitcard_page'),
    path('add-student/', views.create_student, name='add_student'),
    path('update-student/<str:student_id>/', views.update_student, name='update_student'),
    path('delete-student/<str:student_id>/', views.delete_student_confirm, name='delete_student'),
    path('register-courses/<int:id>/', views.course_register_page, name='register_courses'),



    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
