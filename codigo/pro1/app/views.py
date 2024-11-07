from django.shortcuts import render, redirect, get_object_or_404
from app.models import modelo_mas
from app.forms import form_mas
from django.core.exceptions import ValidationError

def index (request):
    return render (request,'app/index.html')

def listado (request):
    model = modelo_mas.objects.all()
    data = {'modelos': model}
    return render (request,'app/listado.html',data)

def agregar (request):
    form = form_mas()
    if request.method == 'POST':
        form = form_mas(request.POST)
        if form.is_valid():
            try:
                form.save()
                return index (request)
            except ValidationError as e:
                form.add_error(None,e)
    
    data = {'form':form,'titulo': 'Agregar Mascota','boton_texto': 'Agregar Mascota'}

    return render ( request, 'app/agregar.html',data)

def eliminar (request,id):
    modelp = modelo_mas.objects.get(id = id)
    modelp.delete()
    return redirect ('/listado')

def actualizar (request,id):
    modelp = modelo_mas.objects.get (id = id)
    form = form_mas(instance=modelp)
    if request.method == 'POST':
        form = form_mas(request.POST, instance=modelp)
        if form.is_valid():
            try:
                form.save()
                return index(request)
            except ValidationError as e:
                form.add_error(None,e)
    data = {'form': form, 'titulo': 'Editar Mascota','boton_texto': 'Guardar Cambios'}
    return render(request,'app/agregar.html',data)