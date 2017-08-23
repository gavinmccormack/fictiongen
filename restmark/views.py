from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from restmark.serializers import UserSerializer, GroupSerializer, BookSerializer
from markov_functions.models import Book

class UserViewSet(viewsets.ModelViewSet):
  """
  API endpoint for viewing/edit of users
  """
  queryset = User.objects.all().order_by('-date_joined')
  serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
  """
  API endpoint for groups to be viewed/edited
  """
  queryset = Group.objects.all()
  serializer_class = GroupSerializer

class GroupViewSet(viewsets.ModelViewSet):
  """
  API endpoint for books to be viewed/edited
  """
  queryset = Book.objects.all()
  serializer_class = BookSerializer