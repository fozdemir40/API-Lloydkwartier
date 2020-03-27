from django.db import models


# Create your models here.
class Moves(models.Model):
    session = models.CharField(max_length=7, default='0')
    location1 = models.BigIntegerField(default=0)
    location2 = models.BigIntegerField(default=0)

    def __str__(self):
        return self.session


class Lobby(models.Model):
    session = models.CharField(max_length=7, default='0')
    playerOne = models.CharField(max_length=50, default='0')
    playerTwo = models.CharField(max_length=50, default='0')
    lobbyCode = models.CharField(max_length=50, default='0')
    moves = models.ForeignKey(Moves, on_delete=models.CASCADE)

    def __str__(self):
        return self.session
