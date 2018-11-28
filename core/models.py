from django.db import models

# Create your models here.



class Raza(models.Model):
    nombre = models.CharField(max_length=80)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Raza"
        verbose_name_plural = "Raza"



class Estado(models.Model):
    TipoEstado = models.CharField(max_length=20)

    def __str__(self):
        return self.TipoEstado

    class Meta:
        verbose_name = "Estado"
        verbose_name_plural = "Estado"

class Genero(models.Model):
    genero = models.CharField(max_length=10)


    def __str__(self):
        return self.genero

    class Meta:
        verbose_name = "Genero"
        verbose_name_plural = "Genero"


class Mascota(models.Model):
    nombre = models.CharField(max_length=50)
    raza = models.ForeignKey(Raza,on_delete=models.CASCADE)
    genero = models.ForeignKey(Genero,on_delete=models.CASCADE)
    fechaIngreso = models.DateField(blank=True)
    fechaNacimiento= models.DateField(null=True, blank=True)
    imagen = models.FileField(upload_to='media',null=True)
    estado = models.ForeignKey(Estado,on_delete=models.CASCADE) 

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Mascota"
        verbose_name_plural = "Mascota"


class tipoVivienda(models.Model):
    nombreV = models.CharField(max_length=30)

    def __str__(self):
        return self.nombreV

    class Meta:
        verbose_name = "Tipo Vivienda"
        verbose_name_plural = "Tipo Vivienda"  


class GeneroP(models.Model):
    generoP = models.CharField(max_length=20)


    def __str__(self):
        return self.generoP

    class Meta:
        verbose_name = "Genero Persona"
        verbose_name_plural = "Genero Persona"


class Region(models.Model):
    nombreR = models.CharField(max_length=50)

    def __str__(self):
        return self.nombreR

    class Meta:
        verbose_name = "Region"
        verbose_name_plural = "Region"  


class Ciudad(models.Model):
    nombreC = models.CharField(max_length=50)

    def __str__(self):
        return self.nombreC

    class Meta:
        verbose_name = "Ciudad"
        verbose_name_plural = "Ciudad"  



class Persona(models.Model):
    correo = models.CharField(max_length=80)
    run = models.CharField(max_length=9)
    nombreP = models.CharField(max_length=80)
    telefono = models.CharField(max_length=9)
    fechaN= models.DateField(null=True, blank=True)
    direccion = models.CharField(max_length=80)
    genero = models.ForeignKey(GeneroP,on_delete=models.CASCADE)
    region = models.ForeignKey(Region,on_delete=models.CASCADE)
    ciudad = models.ForeignKey(Ciudad,on_delete=models.CASCADE)
    tipoV = models.ForeignKey(tipoVivienda,on_delete=models.CASCADE)

    
    def __str__(self):
        return self.nombreP

    class Meta:
        verbose_name = "Persona Agregada"
        verbose_name_plural = "Persona Agregada "