from django.contrib.auth.models import User, Group
from rest_framework import serializers
from pet.models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class AnimalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animales
        fields = ['id', 'nombre', 'edad', 'color', 'raza', 'created_date']