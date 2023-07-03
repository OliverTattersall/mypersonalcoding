"""
URL configuration for drinksData project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from drinksData import views

urlpatterns = [
    path('', views.index, name="index"),
    path('admin/', admin.site.urls),
    path('drink/', views.get_drink, name="get_drink" ),
    path('many/<type>/', views.get_drink_class, name="get_drink_class"),
    path('forms/',views.submit_drink,name="submit_drink"),
    path('heinekendex/', views.heinekendex, name="heinekendex"),
]
