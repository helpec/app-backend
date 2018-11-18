from rest_framework import serializers
from .models import HP_User

class HP_UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = HP_User
        fields = "__all__"