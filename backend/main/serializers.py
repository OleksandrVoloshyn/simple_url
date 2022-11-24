from rest_framework.serializers import ModelSerializer

from .models import MainModel


class MainSerializer(ModelSerializer):
    class Meta:
        model = MainModel
        fields = ('id', 'base', 'short')
