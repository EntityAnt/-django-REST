from rest_framework import serializers

from vehicle.models import Car


class CarSerializer(serializers.Serializer):
    class Meta:
        model = Car
        fields = "__all__"
