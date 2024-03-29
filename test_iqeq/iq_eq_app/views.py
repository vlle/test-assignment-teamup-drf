import random
import string
from datetime import datetime

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from iq_eq_app.models import TestUser
from iq_eq_app.serializers import (EQSerializer, IQSerializer, LoginSerializer,
                                   TestUserSerializer)


def randomword(length):
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for _ in range(length))


@api_view(["POST"])
def initalize_user(request):
    login = randomword(10)
    while TestUser.objects.filter(login=login).first() is not None:
        login = randomword(10)
    registration_data = {"login": login}
    serializer = LoginSerializer(data=registration_data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def save_iq(request):
    user = TestUser.objects.filter(login=request.data["login"]).first()
    if not user:
        return Response(status=status.HTTP_404_NOT_FOUND)
    user.iq_test_time = datetime.now()
    serializer = IQSerializer(user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def save_eq(request):
    user = TestUser.objects.filter(login=request.data["login"]).first()
    if not user:
        return Response(status=status.HTTP_404_NOT_FOUND)
    user.eq_test_time = datetime.now()
    serializer = EQSerializer(user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def view_user(request):
    try:
        user = TestUser.objects.filter(login=request.query_params["login"]).first()
    except KeyError:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if not user:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = TestUserSerializer(user)
    return Response(serializer.data)
