from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from courses.views import CourseListView

urlpatterns = [
    path('', CourseListView.as_view(), name='course_list'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
    path('course/', include('courses.urls')),
    path('students/', include('students.urls')),

]