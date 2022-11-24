from rest_framework import serializers
from .models import RideModel


class RideSerializer(serializers.ModelSerializer):

    class Meta:
        model = RideModel
        fields = "__all__"