from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
# Create your views here.

class PersonView(viewsets.ModelViewSet):
      queryset = Title.objects.all()
      serializer_class = TitleSerializer

class TagView(viewsets.ModelViewSet):
      queryset = Tag.objects.all()
      serializer_class = TagSerializer

class TagTypeView(viewsets.ModelViewSet):
      queryset = Tag_Type.objects.all()
      serializer_class = TagTypeSerializer
