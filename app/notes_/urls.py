from django.urls import path

from . import views

urlpatterns = [
    path("", views.NotesListCreateApiView.as_view()),
    path("<int:pk>", views.NotesRetrieveUpdateDestroyApiView.as_view()),
]
