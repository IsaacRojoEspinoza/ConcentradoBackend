from django.contrib import admin
from django.urls import path, include
from Concentrado import views, userView
from knox import views as knox_views

urlpatterns = [
    # Endpoints para Avance y Nivel
    path('avance/', views.Avance_view, name='Avance_view'),
    path('avanceTotales/', views.avance_totales_view, name='avance_totales_view'),
    path('nivel/', views.Nivel_Api, name='Nivel_Api'),

    # Administración
    path('admin/', admin.site.urls),

    # Endpoints para Periodos y Entidades
    path('periodos/', views.Obtener_periodos_y_entidades, name='obtener_periodos_y_entidades'),

    # Autenticación y gestión de usuarios
    path('api/register/', views.RegisterAPI.as_view(), name='register'),
    path('api/login/', views.LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('check/', views.check_user, name='check_token'),

    # Endpoints adicionales para gestión de usuarios
    path('user/', userView.userViewSet.as_view(), name='user_viewset'),
]
