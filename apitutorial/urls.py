"""apitutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from webapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employees/', views.EmployeesList.as_view()),
    path('api/', include('todo.urls')),
    path('api-auth/', include('rest_framework.urls')), # new
    path('api/v1/dj-rest-auth/', include('dj_rest_auth.urls')), # new
    path('api/v1/dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')), # new
]

# login: http://127.0.0.1:8000/api/v1/dj-rest-auth/login/
# logout: http://127.0.0.1:8000/api/v1/dj-rest-auth/logout/
# reset: http://127.0.0.1:8000/api/v1/dj-rest-auth/password/reset
# password comfirm: http://127.0.0.1:8000/api/v1/dj-rest-auth/password/reset/confirm
# registration http://127.0.0.1:8000/api/v1/dj-rest-auth/registration/
