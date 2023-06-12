from iq_eq_app.models import TestUser
from rest_framework import serializers


class LoginSerializer(serializers.ModelSerializer):
    def validate_login(self, value):
        if len(value) != 10:
            raise serializers.ValidationError("This value should have len = 10")
        return value

    class Meta:
        model = TestUser
        fields = ["login"]


class IQSerializer(serializers.ModelSerializer):
    def validate_iq(self, value):
        if value > 50 or value < 0:
            raise serializers.ValidationError(
                "This value should be in between 0 and 50"
            )
        return value

    class Meta:
        model = TestUser
        fields = ["login", "iq"]


class EQSerializer(serializers.ModelSerializer):
    def validate_eq(self, value):
        for v in value:
            if v not in set(["а", "б", "в", "г", "д"]):
                raise serializers.ValidationError(
                    "This value should be in set ['а', 'б', 'в', 'г', 'д']"
                )
        return value

    class Meta:
        model = TestUser
        fields = ["login", "eq"]


class TestUserSerializer(serializers.ModelSerializer):
    def validate_login(self, value):
        if len(value) != 10:
            raise serializers.ValidationError("This value should have len = 10")
        return value

    def validate_iq(self, value):
        if value > 50 or value < -1:
            raise serializers.ValidationError(
                "This value should be in between -1 (not exists) and 50"
            )
        return value

    def validate_eq(self, value):
        for v in value:
            if v not in set(["а", "б", "в", "г", "д"]):
                raise serializers.ValidationError(
                    "This value should be in set ['а', 'б', 'в', 'г', 'д']"
                )
        return value

    class Meta:
        model = TestUser
        fields = ["login", "iq", "eq", "eq_test_time", "iq_test_time"]
