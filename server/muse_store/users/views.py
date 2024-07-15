from django.contrib.auth.models import Group, User
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from muse_store.users.serializers import GroupSerializer, UserSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all().order_by("name")
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
