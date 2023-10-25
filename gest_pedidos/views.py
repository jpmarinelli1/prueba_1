from django.shortcuts import render,redirect
from django.http import HttpResponse
from gest_pedidos.models import Articulos
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import CustomUserCreationForm

def busqueda_productos(request):

    return render(request, "busqueda_productos.html")

@login_required
def buscar(request):

    if request.GET["prd"]:
        #mensaje= "Arículo buscado %r" %request.GET["prd"]
        producto = request.GET["prd"]

        articulos=Articulos.objects.filter(nombre__icontains=producto) #consulta en base de datos
        

        return render(request, "resultado_busqueda.html", {"nombre":articulos,"query":producto})


    else:
        mensaje= "No hay artículo"
    return HttpResponse(mensaje)

def registrate(request):

    return render(request,"registrate.html")

def exit(request):
    logout(request)
    return redirect('/busqueda_productos/')

def alta_usuario(request):
    data = {
        'form':CustomUserCreationForm()
    }
    if request.method=='POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)

        if user_creation_form.is_valid():
            user_creation_form.save()
            return redirect('/busqueda_productos/')
        else:
            print(user_creation_form.errors)
        
    else:
        print("falló primer if")
    return render(request,"register.html",data )

if __name__ == '__main__': pass

# Create your views here.
