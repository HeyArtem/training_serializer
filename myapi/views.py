from rest_framework import status, viewsets
from rest_framework.generics import ListAPIView  # Var 2
from rest_framework.response import Response
from rest_framework.views import APIView  # Var 1

from .models import Hero
from .serializers import HeroSerializer, ListHeroSerializer


class HeroViewSet(viewsets.ModelViewSet):
    """
    ModelViewSet - это специальное представление, которое предоставляет Django Rest Framework.
    Он будет обрабатывать GET и POST для Heroe без дополнительной работы.
    На практике оно не очень!
    """

    queryset = Hero.objects.all().order_by("name")
    serializer_class = HeroSerializer


class HeroListAPIView(APIView):
    """
    Вар 1, на APIView
    """

    def get(self, request, *args, **kwargs):
        hero = Hero.objects.all().order_by("-id")

        return Response(
            ListHeroSerializer(hero, many=True).data, status=status.HTTP_200_OK
        )


class HeroListAPIViewVAR2(ListAPIView):
    """
    Вар 2, на Дженериках: ListAPIView
    """

    queryset = Hero.objects.all().order_by("-id")
    serializer_class = ListHeroSerializer
