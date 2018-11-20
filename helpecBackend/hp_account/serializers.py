
from django.contrib.auth import get_user_model

from rest_framework import serializers

from .models import Contact, Occurrence

# Get the UserModel
UserModel = get_user_model()


class HP_UserDetailsSerializer(serializers.ModelSerializer):
    """
    User model w/o password
    """
    class Meta:
        model = UserModel
        fields = "__all__"
     
        
class ContactSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Contact
        fields = "__all__"
    

class OccurrenceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Occurrence
        fields = "__all__"
    