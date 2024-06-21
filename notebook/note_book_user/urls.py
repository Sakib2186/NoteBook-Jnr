from django.contrib import admin
from django.urls import path,include
from note_book_user import views

app_name = "note_book_user"

urlpatterns = [
    
    path('login/',views.login_page,name="login_page"),
    path('signup/',views.signup,name="signup"),
    path('dashboard/',views.dashboard,name="dashboard"),
]
