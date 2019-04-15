from rest_framework import viewsets

from .models import Contact, Occurrence
from .serializers import ContactSerializer, OccurrenceSerializer

# Create your views here.
class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.filter(user__is_active=True)
    serializer_class = ContactSerializer

    def get_queryset(self):
        return Contact.objects.filter(user=self.request.user)


class OccurrenceViewSet(viewsets.ModelViewSet):
    queryset = Occurrence.objects.filter(user__is_active=True)
    serializer_class = OccurrenceSerializer

    def get_queryset(self):
        return Contact.objects.filter(user=self.request.user)
