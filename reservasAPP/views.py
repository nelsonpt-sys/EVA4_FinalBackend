from django.shortcuts import render

from reservasAPP.models import *
from reservasAPP.serializers import ReservaSerializer
from rest_framework.response import Response
from rest_framework import status
from reservasAPP.forms import *
from django.http import HttpResponseRedirect
from django.urls import reverse

from rest_framework.decorators import api_view

# Create your views here.


def reservasData(request):
    reservas = Reserva.objects.all()
    data = {'reservas': reservas}
    return render(request, 'reservas.html', data)


def registroReservas(request):
    form = ReservaForm()
    
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('reservas'))
            
    data = {'form': form}  
    return render(request, 'registroReservas.html', data)


def eliminarReservas(request, id):
    reserva = Reserva.objects.get(id=id)
    reserva.delete()
    return HttpResponseRedirect(reverse('reservas'))


def editarReservas(request, id):
    reserva = Reserva.objects.get(id=id)
    form = ReservaForm(instance=reserva)
    
    if request.method == 'POST':
        form = ReservaForm(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('reservas'))
            
    data = {'form': form}  
    return render(request, 'registroReservas.html', data)




def estadosData(request):
    estados = Estado.objects.all()
    data = {'estados': estados}
    return render(request, 'estados.html', data)


def registroEstados(request):
    form = EstadoForm()
    
    if request.method == 'POST':
        form = EstadoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('estados'))
            
    data = {'form': form}  
    return render(request, 'registroEstados.html', data)


def eliminarEstados(request, id):
    estado = Estado.objects.get(id=id)
    estado.delete()
    return HttpResponseRedirect(reverse('estados'))


def editarEstados(request, id):
    estado = Estado.objects.get(id=id)
    form = EstadoForm(instance=estado)
    
    if request.method == 'POST':
        form = EstadoForm(request.POST, instance=estado)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('estados'))
            
    data = {'form': form}  
    return render(request, 'registroEstados.html', data)





@api_view(['GET', 'POST'])
def lista_reservas(request):
    if request.method == 'GET':
        reservas = Reserva.objects.all().order_by('fecha') # Muestra reservas orenadas por fecha
        serializer = ReservaSerializer(reservas, many=True) 
        return Response(serializer.data) 
    
    elif request.method == 'POST':
        serializer = ReservaSerializer(data=request.data) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_201_CREATED) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    


@api_view(['GET', 'PUT', 'DELETE'])
def detalle_reservas(request, pk):
    try:
        reserva = Reserva.objects.get(pk=pk) 
    except Reserva.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ReservaSerializer(reserva) 
        return Response(serializer.data) 
    
    if request.method == 'PUT':
        serializer = ReservaSerializer(reserva, data=request.data) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
    if request.method == 'DELETE':
        reserva.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)