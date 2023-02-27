from rest_framework import serializers

from reviews.models import Category, Genre


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'slug')


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('name', 'slug')


class TitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('name', 'year', 'description', 'genre', 'category', 'rating')
