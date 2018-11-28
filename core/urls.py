from django.urls import path
from .views import home,galeria,formulario,agregar_mascota,listar_mascotas,eliminar_mascota,modificar_mascota
 
urlpatterns = [
    path('', home,name="home"),
    path('galeria/', galeria,name="galeria"),
    path('formulario/', formulario,name="formulario"),
    path('agregar-mascota/', agregar_mascota,name="agregar_mascota"), 
    path('listar-mascotas/', listar_mascotas,name="listar_mascotas"), 
    path('eliminar-mascota/<id>/', eliminar_mascota,name="eliminar_mascota"), 
    path('modificar-mascota/<id>/', modificar_mascota,name="modificar_mascota"), 
]
