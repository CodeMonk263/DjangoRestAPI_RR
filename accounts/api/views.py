from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response
from rest_framework import generics, mixins, permissions

from .serializers import DataSerializer
from accounts.models import Data

class DataListView(generics.ListCreateAPIView):
    serializer_class = DataSerializer
    
    def get_queryset(self):
        qs = Data.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(title__icontains=query)
        return qs

    def perform_create(self, serializer):
        serializer.save(userId=self.request.user)


class DataDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Data.objects.all()
    serializer_class = DataSerializer

    def get_object(self, *args, **kwargs):
        kwargs = self.kwargs
        kw_id = kwargs.get('arg')
        return Data.objects.get(id = kw_id)

