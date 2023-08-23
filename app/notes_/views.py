from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .serializers import NoteSerializer, CreateNoteSerializer
from .models import Note


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user


class NotesListCreateApiView(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permissions_class = (permissions.IsAuthenticated,)
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = ["color", "is_archived"]
    search_fields = ["title", "content"]
    ordering_fields = ["created_at"]
    ordering = ["-created_at"]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)

    def post(self, request):
        serializer = CreateNoteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        note = serializer.save()
        note.author = request.user
        note.save()
        return Response(
            NoteSerializer(note, context=self.get_serializer_context()).data,
            status=status.HTTP_201_CREATED,
        )


class NotesRetrieveUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permissions_class = (permissions.IsAuthenticated, IsOwnerOrReadOnly)
