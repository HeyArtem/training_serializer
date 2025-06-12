from django.shortcuts import render
from rest_framework import viewsets
from .serializers import HeroSerializer
from .models import Hero

class HeroViewSet(viewsets.ModelViewSet):
    '''
    ModelViewSet - это специальное представление, которое предоставляет Django Rest Framework.
    Он будет обрабатывать GET и POST для Heroe без дополнительной работы.
    На практике оно не очень!
    '''
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer


