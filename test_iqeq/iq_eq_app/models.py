from django.db import models


class TestUser(models.Model):
    login = models.CharField(max_length=10, unique=True)
    iq = models.IntegerField(null=True)
    eq = models.CharField(max_length=5, null=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created"]
