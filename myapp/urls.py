
from django.urls import path
from . import views
from .views import student_form_view


urlpatterns = [
    path('home/', views.home, name='home'),
    path('', views.login , name='login'),
    path('menuitem/', views.menuitem, name='menuitem'),
    path('inherit1/', views.inherit1, name='inherit1'),
    path('student/', student_form_view, name='student-form'),
    path('signup/', views.signup, name='signup'),
    path('set-cookie/', views.set_cookie, name='set_cookie'),
    path('get-cookie/', views.get_cookie, name='get_cookie'),
]


