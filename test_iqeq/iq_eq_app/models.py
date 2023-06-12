from django.db import models


class TestUser(models.Model):
    login = models.CharField(max_length=10, unique=True)
    iq = models.IntegerField(null=True)
    iq_test_time = models.DateTimeField(null=True)
    eq = models.CharField(max_length=5, null=True)
    eq_test_time = models.DateTimeField(null=True)
