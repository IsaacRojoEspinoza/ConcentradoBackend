from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from Concentrado.serializers import AvanceSerializer
from Concentrado.models import  Avance,Nivel
from datetime import date
from django.http import JsonResponse
from django.db.models import Count,Sum
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer
from django.contrib.auth import login
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated

@csrf_exempt
    
# def Home_view(request):
#     if request.method == 'GET':
#         completed_task_count = Task.objects.filter(status='COMPLETED').count()
#         ongoing_task_count = Task.objects.filter(status='RUNNING').count()
#         failed_count = Task.objects.filter(status="FAILED").count()

#         all_tasks = Task.objects.all()
#         current_year = date.today().year
#         task_current_year = all_tasks.filter(startDate__year=current_year)

#         tasks_by_month = task_current_year.values('startDate__month', 'status').annotate(task_count=Count('id'))

#         result = {}

#     for month in range(1, 13):
#         result[month] = {'completed': 0, 'running': 0, 'failed': 0}

#     for task_data in tasks_by_month:
#         month = task_data['startDate__month']
#         status = task_data['status']
#         task_count = task_data['task_count']

#         if status == 'COMPLETED':
#             result[month]['completed'] += task_count
#         elif status == 'RUNNING':
#             result[month]['running'] += task_count
#         else:
#             result[month]['failed'] += task_count

#     data = {
#         'completed_task_count': completed_task_count,
#         'ongoing_task_count': ongoing_task_count,
#         'failed_count': failed_count,
#         'graph': result
#     }

#     return JsonResponse(data)
def Total_view(request):
    if request.method == 'GET':
        entidad = request.GET.get('entidad', None)
        if entidad:
            # Filtrar por entidad
            
            queryset = Avance.objects.filter(entidad__exact=entidad)
            
            # Calcular sumas para cada campo deseado
            totalDesignados = queryset.aggregate(total_sum=Sum('numeroDesignados'))['total_sum'] or 0
            totalInscritos = queryset.aggregate(total_sum=Sum('numeroInscritos'))['total_sum'] or 0
            totalIncritosDesignados = queryset.aggregate(total_sum=Sum('inscritosDesignados'))['total_sum'] or 0
            totalConIngreso = queryset.aggregate(total_sum=Sum('conIngreso'))['total_sum'] or 0
            totalConIngresoInscritos = queryset.aggregate(total_sum=Sum('conIngresoInscritos'))['total_sum'] or 0
            totalSinIngreso = queryset.aggregate(total_sum=Sum('sinIngreso'))['total_sum'] or 0
            totalSinIngresoInscritos = queryset.aggregate(total_sum=Sum('sinIngresoInscritos'))['total_sum'] or 0
            totalConcluyeron = queryset.aggregate(total_sum=Sum('concluyeron'))['total_sum'] or 0
            totalConcluyeronDesignados = queryset.aggregate(total_sum=Sum('concluyeronDesignados'))['total_sum'] or 0

            # Preparar el diccionario con todas las sumas
            data = {
                'totalDesignados': totalDesignados,
                'totalInscritos': totalInscritos,
                'totalIncritosDesignados': totalIncritosDesignados,
                'totalConIngreso': totalConIngreso,
                'totalConIngresoInscritos': totalConIngresoInscritos,
                'totalSinIngreso': totalSinIngreso,
                'totalSinIngresoInscritos': totalSinIngresoInscritos,
                'totalConcluyeron': totalConcluyeron,
                'totalConcluyeronDesignados': totalConcluyeronDesignados,
            }
        else:
            queryset = Avance.objects
            totalDesignados = queryset.aggregate(total_sum=Sum('numeroDesignados'))['total_sum'] or 0
            totalInscritos = queryset.aggregate(total_sum=Sum('numeroInscritos'))['total_sum'] or 0
            totalIncritosDesignados = queryset.aggregate(total_sum=Sum('inscritosDesignados'))['total_sum'] or 0
            totalConIngreso = queryset.aggregate(total_sum=Sum('conIngreso'))['total_sum'] or 0
            totalConIngresoInscritos = queryset.aggregate(total_sum=Sum('conIngresoInscritos'))['total_sum'] or 0
            totalSinIngreso = queryset.aggregate(total_sum=Sum('sinIngreso'))['total_sum'] or 0
            totalSinIngresoInscritos = queryset.aggregate(total_sum=Sum('sinIngresoInscritos'))['total_sum'] or 0
            totalConcluyeron = queryset.aggregate(total_sum=Sum('concluyeron'))['total_sum'] or 0
            totalConcluyeronDesignados = queryset.aggregate(total_sum=Sum('concluyeronDesignados'))['total_sum'] or 0
            
            data = {
                'totalDesignados': totalDesignados,
                'totalInscritos': totalInscritos,
                'totalIncritosDesignados': totalIncritosDesignados,
                'totalConIngreso': totalConIngreso,
                'totalConIngresoInscritos': totalConIngresoInscritos,
                'totalSinIngreso': totalSinIngreso,
                'totalSinIngresoInscritos': totalSinIngresoInscritos,
                'totalConcluyeron': totalConcluyeron,
                'totalConcluyeronDesignados': totalConcluyeronDesignados,
            }
    else:
        # En caso de que el método de la solicitud no sea GET
        data = {
            'totalDesignados': 0,
            'totalInscritos': 0,
            'totalIncritosDesignados': 0,
            'totalConIngreso': 0,
            'totalConIngresoInscritos': 0,
            'totalSinIngreso': 0,
            'totalSinIngresoInscritos': 0,
            'totalConcluyeron': 0,
            'totalConcluyeronDesignados': 0,
        }

    return JsonResponse(data)

def avanceApi(request):
    if request.method == 'GET':
        # Captura de parámetros de búsqueda
        entidad = request.GET.get('entidad', None)
        nombreEntidad = request.GET.get('nombreEntidad', None)
        distrito = request.GET.get('distrito', None)

        # Inicia la consulta con todos los registros
        avance_query = Avance.objects.all()

        # Filtrado basado en los parámetros de búsqueda
        if entidad:
            avance_query = avance_query.filter(entidad__exact=entidad)
        if nombreEntidad:
            avance_query = avance_query.filter(nombreEntidad__icontains=nombreEntidad)
        if distrito:
            avance_query = avance_query.filter(distrito__icontains=distrito)

        # Serialización y respuesta
        avance_serializer = AvanceSerializer(avance_query, many=True)
        return JsonResponse(avance_serializer.data, safe=False)

    elif request.method == 'POST':
        avance_data = JSONParser().parse(request)
        avance_serializer = AvanceSerializer(data=avance_data)
        if avance_serializer.is_valid():
            avance_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)

    elif request.method == 'PUT':
        avance_data = JSONParser().parse(request)
        try:
            avance = Avance.objects.get(id=avance_data.get('id'))
        except Avance.DoesNotExist:
            return JsonResponse("Record Not Found", safe=False)
        avance_serializer = AvanceSerializer(avance, data=avance_data)
        if avance_serializer.is_valid():
            avance_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)

    elif request.method == 'DELETE':
        try:
            avance = Avance.objects.get(id=request.GET.get('id'))
        except Avance.DoesNotExist:
            return JsonResponse("Record Not Found", safe=False)
        avance.delete()
        return JsonResponse("Deleted Successfully", safe=False)

def nivelApi(request):
    if request.method == 'GET':
        # Captura de parámetros de búsqueda
        entidad = request.GET.get('entidad', None)

        # Inicia la consulta con todos los registros
        avance_query = Nivel.objects.all()

        # Filtrado basado en los parámetros de búsqueda
        if entidad:
            # Supongo que quieres obtener un único objeto en lugar de una lista
            nivel = avance_query.filter(numeroEntidad__exact=entidad).first()
            
            if nivel:
                # Construir un solo objeto de datos
                data = {
                    'numeroEntidad': nivel.numeroEntidad,
                    'nivelEsperado': nivel.nivelEsperado,
                    'nivelObtenido': nivel.nivelObtenido,
                }
            else:
                # Si no se encuentra ningún objeto, devuelve un objeto vacío o error
                data = {}
        else:
            # Si no se especifica entidad, devuelve un objeto vacío o error
            data = {}

        return JsonResponse(data)
# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
  
        })

# Login API
class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']
        login(request, user)

        # Call the parent class's post method to generate the token response
        return super(LoginAPI, self).post(request, format=None)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def check_user(request):
    try:
        return Response({
            "details": "Token is valid"
        }, status=status.HTTP_200_OK)
    except KeyError:
        return Response({
            "details": "Token is invalid"
        }, status=status.HTTP_400_BAD_REQUEST)