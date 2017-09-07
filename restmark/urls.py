from django.conf.urls import url, include
from . import views
from restmark.views import BookViewSet
from django.contrib.auth.models import User
from rest_framework.routers import DefaultRouter
from rest_framework import serializers, viewsets

# Routers provide an easy way of automatically determining the URL conf.
router = DefaultRouter()
router.register(r'books', views.BookViewSet)


book_list = BookViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'', include(router.urls)),
    url(r'api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
