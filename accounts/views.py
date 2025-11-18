from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated

from .models import CustomUser
from .serializers import UserSerializer
from .filters import UserFilter



class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer



class ProfileView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


    def get_object(self):
        return self.request.user


class UserListView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


    filter_class = UserFilter
    filter_backends = (DjangoFilterBackend,SearchFilter, OrderingFilter)

    search_fields = ["username", "email"]
    ordering_fields = ["username", "email"]