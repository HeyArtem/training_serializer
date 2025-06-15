from django.urls import include, path
from rest_framework import routers

from .views import HeroListAPIView, HeroListAPIViewVAR2, HeroViewSet

router = routers.DefaultRouter()
router.register(r"heroes", HeroViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("api/", include("rest_framework.urls", namespace="rest_framework")),
    # Hero var 1
    path("heros/", HeroListAPIView.as_view()),
    # Hero var 2 (на Дженериках)
    path("herosV2/", HeroListAPIViewVAR2.as_view()),
]
