from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from api.serializers import ManufacturerSerializer, ShoeColorSerializer, ShoeSerializer, ShoeTypeSerializer
from shoeapp.models import Manufacturer, ShoeColor, ShoeType, Shoe


class ManufacturerViewSet(ModelViewSet):
    serializer_class = ManufacturerSerializer
    basename = 'manufacturer'
    queryset = Manufacturer.objects.all()


class ShoeColorViewSet(ModelViewSet):
    serializer_class = ShoeColorSerializer
    basename = 'color'
    queryset = ShoeColor.objects.all()


class ShoeTypeViewSet(ModelViewSet):
    serializer_class = ShoeTypeSerializer
    basename = 'type'
    queryset = ShoeType.objects.all()


class ShoeViewSet(ModelViewSet):
    serializer_class = ShoeSerializer
    baseman = 'shoe'
    queryset = Shoe.objects.all()
