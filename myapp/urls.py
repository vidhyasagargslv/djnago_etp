
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
    
    #cookies
    path('set-cookie/', views.set_cookie, name='set_cookie'),
    path('get-cookie/', views.get_cookie, name='get_cookie'),
    path('delete-cookie/', views.delete_cookie, name='delete_cookie'),
    path('update-cookie/', views.update_cookie, name='update_cookie'),
    #session 
    path('set-session/', views.set_session, name='set_session'),
    path('get-session/', views.get_session, name='get_session'),
    path('delete-session/', views.delete_session, name='delete'),
    path('update-session/', views.update_session, name='update_session'),
]


