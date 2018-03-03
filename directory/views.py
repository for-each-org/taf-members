from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

from rest_framework import viewsets, response, permissions

from .serializers import UserSerializer

# Create your views here.
def index(request):
    return HttpResponse("Hello world, you are at the Directory index!")

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def retrieve(self, request, pk=None):
        if pk == 'i':
            return Response(UserSerializer(request.user,
                context={'request': request}).data)
        return super(UserViewSet, self).retrieve(request, pk)