from django.contrib import admin
from django.urls import path, include
from monica import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('monica.urls')),
]
