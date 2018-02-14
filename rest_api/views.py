from rest_framework import status
from rest_framework.decorators import api_view, detail_route
from rest_framework.response import Response
from rest_framework import viewsets, renderers
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from markov_functions.models import Book
from markov_functions.serializers import BookModelSerializer



class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
