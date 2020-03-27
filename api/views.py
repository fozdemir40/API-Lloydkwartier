from django.shortcuts import render
from rest_framework import viewsets
from .models import Lobby, Moves
from .serializers import LobbySerializer, MovesSerializer


# Create your views here.
class LobbyView(viewsets.ModelViewSet):
    queryset = Lobby.objects.all()
    serializer_class = LobbySerializer


class MovesView(viewsets.ModelViewSet):
    queryset = Moves.objects.all()
    serializer_class = MovesSerializer
