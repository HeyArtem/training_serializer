from rest_framework import viewsets

from .models import Hero
from .serializers import HeroSerializer


class HeroViewSet(viewsets.ModelViewSet):
    """
    ModelViewSet - это специальное представление, которое предоставляет Django Rest Framework.
    Он будет обрабатывать GET и POST для Heroe без дополнительной работы.
    На практике оно не очень!
    """

    queryset = Hero.objects.all().order_by("name")
    serializer_class = HeroSerializer
