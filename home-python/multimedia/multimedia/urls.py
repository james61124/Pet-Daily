"""
URL configuration for multimedia project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from journal import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin', admin.site.urls),
    path('User/Register', views.register),
    path('User/Login', views.login),
    path('get_all_user', views.get_all_user),
    path('delete_user', views.delete_user), 

    path('Shop/GetDressPageInfo', views.GetDressPageInfo),
    path('Diary/UploadImage', views.upload_image),
    path('Diary/UploadDiary', views.upload_diary),
    path('Diary/GetDiaryInfo', views.get_diary_info),

    
    path('Iot/WaterIntake', views.WaterIntake),
    path('Iot/FoodIntake', views.FoodIntake),
    path('Iot/Weight', views.Weight),
]

urlpatterns += static(settings.IMAGE_URL, document_root=settings.IMAGE_ROOT)
