# django related
from django.db.models import fields
from rest_framework import serializers
from .models import MetOfficeWeatherData

class MetOfficeWeatherDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = MetOfficeWeatherData
        fields = "__all__"