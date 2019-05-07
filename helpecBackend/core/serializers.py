from django.contrib.auth import get_user_model
from rest_auth.serializers import PasswordResetSerializer
from rest_framework import serializers

from .models import Contact, Occurrence

# Get the UserModel
UserModel = get_user_model()


class HP_PasswordResetSerializer(PasswordResetSerializer):
    def get_email_options(self):
        """ this method to change default e-mail options"""

        return {
            "subject_template_name": "core/password_reset_subject.txt",
            "email_template_name": "core/password_reset_email.html",
        }


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
        fields = ("id", "name", "phone")
        extra_kwargs = {"id": {"read_only": True}}

    def create(self, validated_data):
        contact = Contact(
            name=validated_data["name"],
            phone=validated_data["phone"],
            user=self.context["request"].user,
        )
        contact.save()
        return contact


class OccurrenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Occurrence
        fields = ("id", "date_creation", "location")
        extra_kwargs = {"id": {"read_only": True}}

    def create(self, validated_data):
        occurrence = Occurrence(
            date_creation=validated_data["date_creation"],
            location=validated_data["location"],
            user=self.context["request"].user,
        )
        occurrence.save()
        return occurrence
