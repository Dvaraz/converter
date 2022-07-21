from django.urls import path

from .views import converter_2

urlpatterns = [
    path('', converter_2),
]