from django.urls import path
from . import views
# отслеживание юрл адрессов
urlpatterns = [
    path('fuf/', views.choto)
]
