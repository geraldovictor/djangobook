from rest_framework import serializers
from .models import Book, BookNumber, Character, Author

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id' , 'name']

class BooKNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookNumber
        fields = ['id', 'isbn_10', 'isbn_13']
        
class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ['id', 'name']

class BookSerializer(serializers.ModelSerializer):
    number = BooKNumberSerializer(many=False)
    characters = CharacterSerializer(many=True)
    authors = AuthorSerializer(many=True)
    class Meta:
        model = Book
        fields = ['id','title', 'price', 'desc' , 'number', 'characters', 'authors']
class BookMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id','title']