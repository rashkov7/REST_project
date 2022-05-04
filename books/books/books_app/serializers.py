from rest_framework import serializers

from books.books_app.models import BookModel


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookModel
        fields = ('title','description','pages')
        # fields = '__all__'

    def validate(self, attrs):
        attrs['author'] = self.initial_data['user']
        return attrs

    def create(self, validated_data):
        return BookModel.objects.create(**validated_data)