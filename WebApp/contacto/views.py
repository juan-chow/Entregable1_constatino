from django.shortcuts import redirect, render
from .forms import FormularioContacto

# Create your views here.
def contacto(request):

    Formulario_Contacto=FormularioContacto()

    if request.method=="POST":
        Formulario_Contacto=FormularioContacto(data=request.POST)
        if Formulario_Contacto.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")

            return redirect("/contacto/?valido")

    return render(request, "contacto/contacto.html",{'miformulario':Formulario_Contacto})