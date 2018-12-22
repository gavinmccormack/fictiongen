from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^old/', views.index),
    url(r'^$', views.storybuilder), 
    url(r'^generator/', views.index)
]
