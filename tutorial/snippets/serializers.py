from rest_framework import serializers
from .models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User


class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style', 'owner']


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'snippets']


class UserSnippetSerializer(serializers.ModelSerializer):
    minLength = serializers.HiddenField(default=10)

    class Meta:
        model = Snippet
        fields = ['title', 'code', 'minLength']

    def validate_title(self, value):
        min_length = self.initial_data['minLength']
        title_length = len(value)

        if title_length < min_length:
            raise serializers.ValidationError("Title is to short! Must be longer than %d" % min_length)

        return value
