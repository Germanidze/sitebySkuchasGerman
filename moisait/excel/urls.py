from django.urls import path
from . import views
# отслеживание юрл адрессов
urlpatterns = [
    path('', views.excelh, name='excelh')
]