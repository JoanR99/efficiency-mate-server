from rest_framework import serializers
from .models import Note


class CreateNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ("title", "content", "color")

        def create(self, validated_data):
            note = Note.objects.create(
                title=validated_data["title"],
                content=validated_data["content"],
                color=validated_data["color"],
            )
            return note


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = "__all__"
