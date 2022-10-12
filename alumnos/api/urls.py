from django.urls import path

from . import views

urlpatterns = [
    path('',views.index),
    path('alumno',views.alumnos),
    path('getalumno',views.getAlumno)
]