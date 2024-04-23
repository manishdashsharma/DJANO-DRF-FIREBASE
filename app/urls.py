from django.urls import path
from .views import *

urlpatterns = [
    path('', service_info.as_view())
]