from django.http import JsonResponse

def index(request):
    context = {
        'mensaje':'Bienvenido a mi primer API con Django'
    }
    return JsonResponse(context)

from .models import Alumno

def alumnos(request):
    dataAlumnos = Alumno.objects.all()
    print(dataAlumnos)
    #serializacion
    listaAlumnos = []
    for alumno in dataAlumnos:
        dicAlumno = {
            'nombre':alumno.nombre,
            'email':alumno.email
        }
        listaAlumnos.append(dicAlumno)
    
    context = {
        'content':listaAlumnos
    }

    return JsonResponse(context)

########### aplicando django restframework ##########
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import AlumnoSerializer

@api_view(['GET'])
def getAlumno(request):
    dataAlumnos = Alumno.objects.all()
    serAlumnos = AlumnoSerializer(dataAlumnos,many=True)

    context = {
        'status':True,
        'content':serAlumnos.data
    }

    return Response(context)