from django.urls import path
from .views import crop_predict

urlpatterns = [
    path("predict/", crop_predict),
]
