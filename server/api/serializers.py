from typing import ClassVar

from django.contrib.auth.models import Group, User
from rest_framework.serializers import HyperlinkedModelSerializer


class UserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields: ClassVar = ["url", "username", "email", "groups"]

class GroupSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields: ClassVar = ["url", "name"]
