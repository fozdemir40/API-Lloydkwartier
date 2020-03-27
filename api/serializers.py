from rest_framework import serializers
from .models import Lobby, Moves


# Serializers here

class MovesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moves
        fields = ('id', 'session', 'location1', 'location2')


class LobbySerializer(serializers.ModelSerializer):
    class Meta:
        model = Lobby
        fields = ('id', 'session', 'playerOne', 'playerTwo', 'lobbyCode', 'moves')


class BundleSerializer(serializers.ModelSerializer):
    moves = MovesSerializer()

    class Meta:
        model = Lobby
        fields = ('id', 'session', 'playerOne', 'playerTwo', 'lobbyCode', 'moves')

