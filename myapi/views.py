from rest_framework import status, viewsets
from rest_framework.generics import ListCreateAPIView  # Var 2
from rest_framework.response import Response
from rest_framework.views import APIView  # Var 1

from .models import Hero
from .serializers import HeroSerializer, HeroSerializerS


class HeroViewSet(viewsets.ModelViewSet):
    """
    ModelViewSet - это специальное представление, которое предоставляет Django Rest Framework.
    Он будет обрабатывать GET и POST для Heroe без дополнительной работы.
    На практике оно не очень!
    """

    queryset = Hero.objects.all().order_by("name")
    serializer_class = HeroSerializerS


class HeroListCreateAPIView(APIView):
    """
    Вар 1, на APIView
    """

    def get(self, request, *args, **kwargs) -> Response:
        hero = Hero.objects.all().order_by("-id")

        # query_params -> dict
        # query_params["search"] -> Error
        # query_params.get ("search") -> Value or None
        search = request.query_params.get("search")
        print("[!] search: ", search)
        if search:
            hero = hero.filter(name__icontains=search)
            print("[!] hero: ", hero)

        return Response(HeroSerializer(hero, many=True).data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs) -> Response:
        "Create"
        serializer = HeroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HeroListCreateAPIViewVAR2(ListCreateAPIView):
    """
    Вар 2, на Дженериках
    """

    serializer_class = HeroSerializer

    def get_queryset(self):
        return Hero.objects.filter(
            name__icontains=self.request.query_params.get("search", "")
        )
