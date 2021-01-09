from django.urls import path
from MailerApp.views import *

urlpatterns = [
    path('mail/', MailAPIView.as_view()),
]