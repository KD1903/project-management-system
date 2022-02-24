"""pms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url
from django.conf.urls.static import static

from users.views import user_login, register, logout_user, dashboard
from projects.views import create_project, view_project, change_tasks

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', user_login, name='login'),
    path('login/', user_login, name='login'),
    path('register/', register, name='register'),
    path('logout_user/', logout_user, name='logout_user'),

    path('dashboard/', dashboard, name='dashboard'),
    path('create_project', create_project, name='create_project'),
    url(r'change_tasks/$', change_tasks, name='change_tasks'),
    url(r'view_project/$', view_project, name='view_project'),
]
