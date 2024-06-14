from django.shortcuts import get_object_or_404
from rest_framework import viewsets

# Create your views here.

from car.models import Car, Reservation
from car.serializers import CarSerializer, ReservationSerializer


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
