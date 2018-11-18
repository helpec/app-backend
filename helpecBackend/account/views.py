
from rest_framework import generics
from .models import HP_User
from .serializers import HP_UserSerializer

# Create your views here.

class HP_UserListAPIView(generics.ListCreateAPIView):
    queryset = HP_User.objects.filter(is_active=True)
    serializer_class = HP_UserSerializer
    