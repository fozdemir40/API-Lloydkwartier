from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('lobby', views.LobbyView)
router.register('moves', views.MovesView)

urlpatterns = [
    path('', include(router.urls))
]