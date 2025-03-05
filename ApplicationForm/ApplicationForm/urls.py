"""
URL configuration for ApplicationForm project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from testapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.page_1_view),
    path('page2', views.page_2_view),
    path('page3', views.page_3_view),
    path('page4', views.page_4_view),
    path('page5', views.page_5_view),
    path('page6', views.page_6_view),
    path('page7', views.page_7_view),
    path('page8', views.page_8_view),
    path('page9', views.page_9_view),

]
