from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='name'), 
    path('storage/<str:placa>/<int:modelo>/<str:marca>/<int:cedula>',views.storage   ,name="storage"),
    # path('consultar/<int:id>',views.consultar,name="consultar"),
    # path('modificar/<int:id>/<str:titulo>/',views.modificar,name="modificar"),
    # path('eliminar/<int:id>',views.eliminar,name="eliminar"),
    path('storage_conductor/<int:cedula>/<str:nombre>/<str:apellido>/<int:telefono>/<str:correo>/<str:direccion>/',views.storage_conductor   ,name="storage_conductor"),
    # path('consultas',views.consultas,name="consultas"),

]
