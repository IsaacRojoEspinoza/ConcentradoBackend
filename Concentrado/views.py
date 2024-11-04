from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .serializers import AvanceSerializer, NivelSerializer, UserSerializer, RegisterSerializer
from .models import Avance, Nivel, Entidad, Periodo
from django.db.models import Sum
from knox.models import AuthToken
from django.contrib.auth import login
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

@csrf_exempt
@api_view(['GET'])
def Obtener_periodos_y_entidades(request):
    periodos = Periodo.objects.all()
    data = []

    for periodo in periodos:
        entidades = Entidad.objects.filter(avances__periodo=periodo).distinct()
        data.append({
            'periodo_id': periodo.id,
            'anio_inicio': periodo.anio_inicio,
            'anio_fin': periodo.anio_fin,
            'entidades': [
                {
                    'id': entidad.numero,
                    'nombre': entidad.nombre_entidad,
                    'logo': entidad.logo,
                }
                for entidad in entidades
            ]
        })

    return Response(data)

def avance_totales_view(request):
    if request.method == 'GET':
        entidad_id = request.GET.get('entidad', None)
        queryset = Avance.objects.filter(entidad__numero=entidad_id) if entidad_id else Avance.objects.all()

        data = {
            'total_designados': queryset.aggregate(total=Sum('numero_designados'))['total'] or 0,
            'total_inscritos': queryset.aggregate(total=Sum('numero_inscritos'))['total'] or 0,
            'total_inscritos_designados': queryset.aggregate(total=Sum('inscritos_designados'))['total'] or 0,
            'total_con_ingreso': queryset.aggregate(total=Sum('con_ingreso'))['total'] or 0,
            'total_con_ingreso_inscritos': queryset.aggregate(total=Sum('con_ingreso_inscritos'))['total'] or 0,
            'total_sin_ingreso': queryset.aggregate(total=Sum('sin_ingreso'))['total'] or 0,
            'total_sin_ingreso_inscritos': queryset.aggregate(total=Sum('sin_ingreso_inscritos'))['total'] or 0,
            'total_concluyeron': queryset.aggregate(total=Sum('concluyeron'))['total'] or 0,
            'total_concluyeron_designados': queryset.aggregate(total=Sum('concluyeron_designados'))['total'] or 0,
        }

        return JsonResponse(data)
@csrf_exempt
def Avance_view(request):
    if request.method == 'GET':
        entidad_id = request.GET.get('entidad', None)
        nombre_entidad = request.GET.get('nombre_entidad', None)
        distrito = request.GET.get('distrito', None)

        avance_query = Avance.objects.all()

        if entidad_id:
            avance_query = avance_query.filter(entidad__numero=entidad_id)
        if nombre_entidad:
            avance_query = avance_query.filter(entidad__nombre_entidad__icontains=nombre_entidad)
        if distrito:
            avance_query = avance_query.filter(distrito=distrito)

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

@csrf_exempt
def Nivel_Api(request):
    if request.method == 'GET':
        # Obtén el ID de la entidad desde los parámetros de consulta
        entidad_id = request.GET.get('entidad', None)  
        
        response_data = {}

        if entidad_id:
            nivel = Nivel.objects.filter(entidad__numero=entidad_id).first()
            if nivel:
                response_data = {
                    'numero_entidad': nivel.entidad.numero,
                    'nivel_esperado': nivel.nivel_esperado,
                    'nivel_obtenido': nivel.nivel_obtenido,
                }
            else:
                response_data = {'error': 'No se encontró nivel para la entidad especificada.'}
        else:
            response_data = {'error': 'El ID de la entidad es requerido.'}

        return JsonResponse(response_data)

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
        return super(LoginAPI, self).post(request, format=None)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def check_user(request):
    return Response({"details": "Token is valid"}, status=status.HTTP_200_OK)
