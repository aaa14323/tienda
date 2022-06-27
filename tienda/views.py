from django.shortcuts import render
from django.http import HttpResponse
from tienda.models import Producto, Cliente
from tienda.modelForms import ProductoForm, ClienteForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def producto_index(request):
    p = Producto.objects.all()
    context = {
        'producto': p
    }
    return render(request, 'producto_index.html', context)

def imagenes(request):
    p = Producto.objects.all()
    context = {
        'producto': p
    }
    return render(request, 'creditos-imagenes.html', context)


def cliente_add(request):
    if request.method == 'POST':
        formr = ClienteForm(request.POST)
        if formr.is_valid():
            formr.save()
            return cliente_index(request)
    else:
        formset = ClienteForm()
    return render(request, 'cliente_add.html', {'mform': formset})

def producto_add(request):
    if request.method == 'POST':
        formpro = ProductoForm(request.POST)
        if formpro.is_valid():
            formpro.save()
            return producto_index(request)
    else:
        formpro = ProductoForm()
    return render(request, 'producto_add.html', {'mformpr': formpro})


def cliente_index(request):
    c = Cliente.objects.all()
    context = {
        'cliente': c
    }
    return render(request, 'cliente_index.html', context)

def compra(request):
    c = Cliente.objects.all()
    p = Producto.objects.all()
    context = {
        'cliente': c,
        'producto': p
    }
    return render(request, 'compras.html', context)

def compra_producto(request):
    p = Producto.objects.all()
    context = {
        'producto': p
    }
    return render(request, 'compras_productos.html', context)

def delete_cliente(request, idc):
    try:
        c1 = Cliente.objects.get(id=idc)
        c1.delete()
        return cliente_index(request)
    except:
        print('')
        return cliente_index(request)

def delete_producto(request, idp):
    try:
        p1 = Producto.objects.get(id=idp)
        p1.delete()
        return producto_index(request)
    except:
        print('')
        return producto_index(request)

def update_cliente(request, idcl):
    cl1 = Cliente.objects.get(id=idcl)
    if request.method == 'GET':
        form = ClienteForm(instance=cl1)
        return render(request, 'update_cliente.html',{'mform':form})
    elif request.method == 'POST':
        form = ClienteForm(request.POST, instance=cl1)
        if form.is_valid():
            form.save()
        return cliente_index(request)

def update_producto(request, idpr):
    pr1 = Producto.objects.get(id=idpr)
    if request.method == 'GET':
        formp = ProductoForm(instance=pr1)
        return render(request, 'update_producto.html', {'mformp': formp})
    elif request.method == 'POST':
        formp = ProductoForm(request.POST, instance=pr1)
        if formp.is_valid():
            formp.save()
        return producto_index(request)

