from django.shortcuts import render
from django.http import HttpResponse
from .models import Conductor,Auto

# Create your views here.
def index(request):
  conductores = Conductor.objects.all()
  for obj in conductores:
    print("Nombre : ",obj.nombre)
  return HttpResponse('lista de conductores')
  
def  storage(request,placa,modelo,marca,cedula):
  conductor = Conductor.objects.get(id=cedula)
  print(f'{placa},{modelo},{marca},{cedula}')
  post = Auto(placa=placa, modelo=modelo, marca=marca, cedula=cedula)
  post.save()
  print(conductor)
  return HttpResponse(f'Guardamos los datos{conductor}')

def  storage_conductor(request,cedula,nombre,apellido,telefono,correo,direccion):
  post = Conductor(cedula=cedula, nombre=nombre, apellido=apellido, telefono=telefono, correo=correo, direccion=direccion)
  post.save()
  print(nombre)
  return HttpResponse('Guardamos Conductor')

# def  consultar (request, id):
#   post = Post.objects.get(id=id) #trae el registro que coincida con la llave primaria

#   print (post)
#   return HttpResponse (f"Nombre: {post.titulo}, Cuerpo: {post.cuerpo}, fecha: {post.fecha}, autor: {post.autor}")  
  
# def  modificar(request,titulo,id):
    
#   post = Post.objects.get(id=id)
#   post.titulo = titulo
#   post.save()

#   return HttpResponse ('Se actualizaron los Datos')

# def eliminar(request,id):
#   post = Post.objects.get(id=id)
#   post.delete()
#   return HttpResponse ("Registro Eliminado")
