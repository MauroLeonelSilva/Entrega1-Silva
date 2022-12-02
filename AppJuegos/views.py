from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from AppJuegos.forms import *

# Create your views here.


def inicio(request):
    

    return render (request, "AppJuegos/inicio.html")


def videoJuegos(request):
    if request.method=="POST":
        form=VideojuegosForm(request.POST)
        
        if form.is_valid():

            informacion=form.cleaned_data
            
            nombreform=informacion["nombre"]
            calificacionform=informacion["calificacion"]
            generoform=informacion["genero"]

            juegoguardado=VideoJuegoModel(nombre=nombreform, calificacion=calificacionform, genero=generoform)
            juegoguardado.save()
            return render (request, "AppJuegos/inicio.html", {"mensaje": "juego subido a la base de datos"})
    else:
        formulario=VideojuegosForm()

    return render (request, "AppJuegos/videojuegos.html", {"form": formulario})


def juegosdemesa(request):
    if request.method=="POST":
        form=juegosdemesaform(request.POST)
        
        if form.is_valid():

            informacion=form.cleaned_data

            Nombrejuegoform=informacion["Nombrejuego"]
            Tipo_juegoform=informacion["Tipo_juego"]
            Cantidad_jugadoresform=informacion["Cantidad_jugadores"]

            juegoguardado=juegosdemesaModel(Nombrejuego=Nombrejuegoform, Tipo_juego=Tipo_juegoform, Cantidad_jugadores=Cantidad_jugadoresform)
            juegoguardado.save()
            return render (request, "AppJuegos/inicio.html", {"mensaje": "juego de mesa subido a la base de datos"})
    else:
        formulario=juegosdemesaform()

    return render (request, "AppJuegos/juegosdemesa.html", {"form": formulario})

    

def cartas(request):
    carta1=carta(Nombrejuego="magic", Nombrecarta="aniquilador", Rareza="rara")
    
    carta1.save()
    cadena_Texto="carta guardada: "+cartas.Nombrejuego+" "+cartas.Nombrecarta+" "+cartas.Rareza
    return HttpResponse(cadena_Texto)
    



def juegosdecartas(request):

    if request.method=="POST":
        form=CartasForm(request.POST)
    
        if form.is_valid():
            informacion=form.cleaned_data
            print(informacion)
            juegoform=informacion["juego"]
            cartaform=informacion["nombre_carta"]
            rarezaform=informacion["rareza"]

            cartaguardada=carta(Nombrejuego=juegoform, Nombrecarta=cartaform, Rareza=rarezaform)
            cartaguardada.save()
            return render (request, "AppJuegos/inicio.html")
    else:
        formulario=CartasForm()

    return render (request, "AppJuegos/juegosdecartas.html", {"form": formulario})


def busquedaCartas(request):
    return render (request, "AppJuegos/busquedaCartas.html")

def buscar(request):

    if request.GET["Nombrejuego"]:

        Nombrejuego=request.GET["Nombrejuego"] #all trae todos, filter trae uno o mas si los encuentra y si no trae la lista vacia, y get trae uno  
        print(Nombrejuego)                       
        cartas=carta.objects.filter(Nombrejuego=Nombrejuego) 
        print(cartas)      
        

        return render (request, "AppJuegos/resultadosBusqueda.html", {"cartas": cartas})
    else:
        return render (request, "AppJuegos/busquedaCartas.html", {"mensaje":"ingresa algún juego de cartas (TCG)"})

    