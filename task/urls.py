from django.contrib import admin
from django.urls import path
from django.urls import include
from .views import CreateUniqueIdentifier
urlpatterns = [
    path('<str:namespace>', CreateUniqueIdentifier.as_view()),
]
