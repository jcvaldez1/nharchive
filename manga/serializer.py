from rest_framework import serializers
from .models import *

class TitleSerializer(serializers.ModelSerializer):
      class Meta:
            model = Title
            fields = ('japanese' , 'pretty', 'english')

class TagSerializer(serializers.ModelSerializer):
      class Meta:
            model = Title
            fields = ('url' , 'count', 'tag_type', 'tag_id', 'name')

class TagTypeSerializer(serializers.ModelSerializer):
      class Meta:
            model = Tag_Type
            fields = ['tag_name']

class BookSerializer(serializers.ModelSerializer):
      class Meta:
            model = Book
            fields = ('upload_date', 'book_id', 'media_id', 'num_favorites', 'num_pages', 'scanlator', 'tags', 'title')
