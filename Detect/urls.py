
from django.urls import path

from .views import views

urlpatterns = [
    path('detect/', views.classify_flower, name='detect'),
]
