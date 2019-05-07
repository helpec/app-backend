from django.http import HttpResponse
from django.views import View
from rest_framework import viewsets


from .models import Contact, Occurrence
from .serializers import ContactSerializer, OccurrenceSerializer


class HomePage(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Hello, World!")


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
