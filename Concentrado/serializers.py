from rest_framework import serializers
from Concentrado.models import Avance, Nivel, Entidad, Periodo
from django.contrib.auth.models import User

class AvanceSerializer(serializers.ModelSerializer):
    entidad = serializers.StringRelatedField()  # Muestra el nombre de la entidad en vez de su ID
    periodo = serializers.StringRelatedField()  # Muestra el periodo en formato 'anio_inicio-anio_fin'

    class Meta:
        model = Avance
        fields = '__all__'

class NivelSerializer(serializers.ModelSerializer):
    entidad = serializers.StringRelatedField()  # Muestra el nombre de la entidad en vez de su ID
    periodo = serializers.StringRelatedField()  # Muestra el periodo en formato 'anio_inicio-anio_fin'

    class Meta:
        model = Nivel
        fields = '__all__'

class EntidadSerializer(serializers.ModelSerializer):
    # Serializa los niveles y avances asociados a la entidad
    niveles = NivelSerializer(many=True, read_only=True)
    avances = AvanceSerializer(many=True, read_only=True)

    class Meta:
        model = Entidad
        fields = '__all__'

class PeriodoSerializer(serializers.ModelSerializer):
    # Serializa los avances y niveles asociados al periodo
    avances = AvanceSerializer(many=True, read_only=True)
    niveles = NivelSerializer(many=True, read_only=True)

    class Meta:
        model = Periodo
        fields = '__all__'

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'is_superuser', 'first_name', 'last_name', 'email']
        extra_kwargs = {
            'password': {
                'write_only': True,
            },
        }

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
