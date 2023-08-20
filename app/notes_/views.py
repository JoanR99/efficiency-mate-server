from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .serializers import NoteSerializer, CreateNoteSerializer
from .models import Note


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user


class NotesListCreateApiView(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permissions_class = (permissions.IsAuthenticated,)

    def get(self, request):
        notes = Note.objects.filter(author=request.user.id)
        serializer = self.get_serializer(notes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CreateNoteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        note = serializer.save()
        note.author = request.user
        note.save()
        return Response(
            {
                "note": NoteSerializer(
                    note, context=self.get_serializer_context()
                ).data,
                "message": "Note Created Successfully",
            },
            status=status.HTTP_201_CREATED,
        )


class NotesRetrieveUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permissions_class = (permissions.IsAuthenticated, IsOwnerOrReadOnly)
