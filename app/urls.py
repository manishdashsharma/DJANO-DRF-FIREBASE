from django.urls import path
from .views import *

urlpatterns = [
    path('', serviceInfo.as_view()),
    path('user/', user_info.as_view())
]