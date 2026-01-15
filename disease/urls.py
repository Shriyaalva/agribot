from django.urls import path
from .views import disease_predict

urlpatterns = [
    path("predict/", disease_predict),
]
