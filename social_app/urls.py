from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views
from django.urls import path

app_name = 'social_app'

urlpatterns=[
    path('login/',auth_views.LoginView.as_view(template_name='social_app/login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(), name='logout'),
    path('signup/',views.Signup.as_view(),name='signup'),
]

