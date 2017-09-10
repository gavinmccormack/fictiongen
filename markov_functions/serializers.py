from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Book



class BookModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('name', 'file', 'model', 'user', 'created', 'lines', 'sentences')

# this may be needed to customize the serializer in future but for now is unused
        """class BookSerializer(serializers.Serializer):
        name = serializers.CharField(read_only=False)
        file = serializers.FileField(max_length=None, allow_empty_file=False)
        model = serializers.FileField(max_length=None, allow_empty_file=True)
        user = serializers.RelatedField(many=False, read_only=True)
        created = serializers.DateTimeField()
        modified = serializers.DateTimeField()
        lines = serializers.IntegerField(read_only=False)
        sentences = serializers.IntegerField(read_only=False)

        def create(self, validated_data):
            return Book.objects.create(**validated_data)

            def update(self, validated_data):
                instance.name = validated_data.get('name', instance.name)
                instance.file = validated_data.get('file', instance.file)
                instance.model = validated_data.get('model', instance.model)
                instance.user = validated_data.get('user', instance.user)
                instance.created = validated_data.get('created', instance.created)
                instance.modified = validated_data.get('modified', instance.modified)
                instance.lines = validated_data.get('lines', instance.lines)
                instance.sentences = validated_data.get('sentences', instance.sentences)
                instance.save()
                return instance"""
