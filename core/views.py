from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Mascota,Raza,Genero,Estado,tipoVivienda,GeneroP,Region,Ciudad,Persona   
from django.contrib import messages
# Create your views here.


def home(request):
    return render(request,'core/home.html')

def galeria(request):
    return render(request, 'core/galeria.html')

def formulario(request):

    genero = GeneroP.objects.all()
    region = Region.objects.all()
    ciudad = Ciudad.objects.all()
    vivienda = tipoVivienda.objects.all()

    variables = {

        'genero' : genero,
        'region' : region,
        'ciudad' : ciudad,
        'vivienda' : vivienda,
    }

    if request.POST:
        persona = Persona()
        persona.correo = request.POST.get('txtCorreo')
        persona.run = request.POST.get('txtRun')
        persona.nombreP = request.POST.get('txtNombreCompleto')
        persona.telefono = request.POST.get('txtTelefono')
        persona.fechaN = request.POST.get('txtFecha')
        persona.direccion = request.POST.get('txtDireccion')

        sexoo = GeneroP()
        sexoo.id = request.POST.get('cboGenero')
        persona.genero = sexoo
       
        regionC = Region()
        regionC.id = request.POST.get('cboRegion')
        persona.region = regionC
       
        ciudadId = request.POST.get('cboCuidad')
        
        ciudadS = Ciudad()
        ciudadS.id = ciudadId
        persona.ciudad = ciudadS

        viviendaG = tipoVivienda()
        viviendaG.id = request.POST.get('cboVivienda')
        persona.tipoV = viviendaG

        persona.save()
        try:
            variables['mensaje'] = 'Guardado Correctamente'
       
        except:
            variables['mensaje'] = 'No se ha podido guardar'


    return render(request, 'core/formulario.html',variables)

@login_required
def agregar_mascota(request):

    perri = Raza.objects.all()
    sexo = Genero.objects.all()
    estado = Estado.objects.all()
    raza = Raza.objects.all()
    variables = {
        'perri':perri,
        'sexo':sexo,
        'estado':estado,
        'raza': raza,
    }


    if request.POST:
        perro = Mascota()
        perro.nombre = request.POST.get('txtNombre')

        razita = Raza()
        razita.id = request.POST.get('cboRaza')
        perro.raza = razita

        sexo = Genero()
        sexo.id = request.POST.get('cboGenero')
        perro.genero = sexo

        perro.fechaIngreso = request.POST.get('txtFechaI')

        if request.POST.get('txtFechaN') != '':
            perro.fechaNacimiento = request.POST.get('txtFechaN')

        perro.imagen = request.FILES.get('txtFoto')

        estadito = Estado()
        estadito.id = request.POST.get('cboEstado')
        perro.estado = estadito

        perro.razita = Mascota
        perro.sexo = Mascota
        perro.estadito = Mascota
        perro.save()

        try:
            variables['mensaje'] = 'Guardado Correctamente'
        except:
            variables['mensaje'] = 'No se ha podido guardar'

    return render(request, 'core/agregar_mascota.html',variables)

#crud mascotas

def listar_mascotas(request):

    mascotas = Mascota.objects.all()

    return render(request,'core/listar_mascotas.html',{
        'mascotas':mascotas 
    })


def eliminar_mascota(request,id):
    #buscar la mascota que deseamos eliminar
    mascota = Mascota.objects.get(id=id)

    try:
        mascota.delete()
        mensaje = "Eliminado Correctamente"
        messages.success(request,mensaje)
    except:
        mensaje = "No se ha podido eliminar"
        messages.error(request,mensaje)

    return redirect('listar_mascotas')


def modificar_mascota(request, id):
    #buscamos el id de la mascota
    mascota = Mascota.objects.get(id=id)
    estado = Estado.objects.all()
    raza = Raza.objects.all()
    sexo = Genero.objects.all()
    variables = {
        'mascota': mascota,
        'estado' : estado,
        'raza' : raza,
        'sexo' : sexo,
    }
    
    return render(request, 'core/modificar_mascota.html', variables)

