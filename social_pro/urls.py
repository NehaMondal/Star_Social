"""social_pro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import include
from django.urls import path
from . import views

urlpatterns = [
    path('',views.HomePage.as_view(),name='home'),
    path('admin/', admin.site.urls),
    path('social_app/',include('social_app.urls',namespace='accounts')),
    path('social_app/',include('django.contrib.auth.urls')),
    path('test/',views.TestPage.as_view(),name='test'),
    path('thanks/',views.ThanksPage.as_view(),name='thanks'),
    path('posts/',include('posts.urls', namespace='posts')),
    path('groups/',include('groups.urls', namespace='groups'))
]
