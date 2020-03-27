from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Lobby', views.LobbyView)
router.register('Moves', views.MovesView)

urlpatterns = [
    path('', include(router.urls))
]