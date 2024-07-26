from django.db import models


class Subscriber(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    number = models.IntegerField(verbose_name="Number")
    tech = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.number}"


class Control(models.Model):
    subscriber = models.ForeignKey(Subscriber, on_delete=models.CASCADE)
    online = models.DateTimeField(verbose_name="Online", auto_now_add=True)
    offline = models.DateTimeField(null=True, blank=True, verbose_name="Offline")

    def __str__(self):
        return f"{self.subscriber} - {self.online}"


