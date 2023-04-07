from django.urls import path
from .views import index, BirthdayMessageView

urlpatterns = [
    path('', index, name='index'),
    path('messages/', BirthdayMessageView.as_view(), name='birthday_messages'),
]
