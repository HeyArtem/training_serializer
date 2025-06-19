from rest_framework import serializers

from .models import Hero

"""
    Все сериалайзеры
"""


class HeroSerializer(serializers.ModelSerializer):
    """
    Дефолтный сериалайзер.
        APIView: чтение & Создание
        Дженерики: чтение и создание
    """

    class Meta:
        model = Hero
        fields = [
            "id",
            "name",
            "alias",
            "content",
            "date_of_birth",
            "created_at",
            "updated_at",
        ]


class HeroSerializerS(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        fields = ("id", "name", "alias")
