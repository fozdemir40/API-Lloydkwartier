from rest_framework import serializers
from .models import Lobby, Moves


# Serializers here

class LobbySerializer(serializers.ModelSerializer):
    class Meta:
        model = Lobby
        fields = ('id', 'session', 'playerOne', 'playerTwo', 'lobbyCode', 'moves')


class MovesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moves
        fields = ('id', 'location1', 'location2')
