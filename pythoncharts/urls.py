"""pythoncharts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path,include
#from django.urls import include
from pythoncharts.views import chartcreation,registerview,dashboardview
from pythoncharts.someview import something, trainingdue, lrdue
from django.contrib.auth.views import LoginView,LogoutView
#from pythoncharts.registerview import register_request



urlpatterns = [
    #path('', views.chartcreation, name='chartcreation'),
    path('', dashboardview),
    path('pythoncharts/', chartcreation),
    path('prdue/', something),
    path('trainingdue/', trainingdue),
    path('lrdue/', lrdue),
    path('login/',LoginView.as_view(), name = "login"),
    path('register/', registerview, name = "register"),
    path('admin/', admin.site.urls),
    path('logout/',LogoutView.as_view(), name = "logout"),
    #path('register/', register_request, name="register"),
]
