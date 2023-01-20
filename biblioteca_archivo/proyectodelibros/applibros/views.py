from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import FormLibro
from . models import libros

# Create your views here.
def index(request):
    libro1=libros.objects.all()
    context={
        'libro_lista': libro1
    }
    return render(request, 'index.html', context)


def detail(request, libro_id):
    libro = libros.objects.get(id=libro_id)
    return render(request, "detail.html", {'libro':libro})

def add_libro(request):
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        year = request.POST.get('year')
        img = request.FILES['img']
        libro = libros(name=name, description=description, year=year, img=img)
        libro.save()
        return redirect('/')
    return render(request, 'add.html')

def update(request, id):
    libro = libros.objects.get(id=id)
    form = FormLibro(request.POST or None, request.FILES, instance=libro)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'form':form, 'libro':libro})

def eliminar(request, id):
    if request.method=='POST':
        libro = libros.objects.get(id=id)
        libro.delete()
        return redirect('/')
    return render(request, 'eliminar.html')
