from django.db import models
from django.contrib.auth.models import User


class Server(models.Model):
    name = models.CharField(max_length=200)
    ip = models.GenericIPAddressField()
    port = models.IntegerField()
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    content = models.TextField()

    status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.ip}:{self.port}"


class Costumer(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    server = models.ForeignKey(Server, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.user} : {self.server}"

