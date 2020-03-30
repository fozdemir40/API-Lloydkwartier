from django.shortcuts import render
from rest_framework import viewsets, permissions, generics, routers
from .models import Lobby, Moves
from .serializers import LobbySerializer, MovesSerializer, BundleSerializer
from django.utils.safestring import mark_safe


# Create your views here.
class LobbyView(viewsets.ModelViewSet):
    queryset = Lobby.objects.all()
    serializer_class = LobbySerializer


class MovesView(viewsets.ModelViewSet):
    queryset = Moves.objects.all()
    serializer_class = MovesSerializer


class BundleView(generics.ListAPIView):
    queryset = Lobby.objects.all()
    serializer_class = BundleSerializer


class MyAPIRootView(routers.APIRootView):
    """
    Controls appearance of the API root view
    """

    def get_view_name(self) -> str:
        return "Root"

    def get_view_description(self, html=False) -> str:
        text = "This API is made for the interactive object 'Battleship'"
        if html:
            return mark_safe(f"<p>{text}</p>")
        else:
            return text


class MyRouter(routers.DefaultRouter):
    APIRootView = MyAPIRootView

