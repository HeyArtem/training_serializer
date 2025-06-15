from rest_framework import serializers

from .models import Hero


class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        fields = ("id", "name", "alias")


class ListHeroSerializer(serializers.ModelSerializer):
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
