from django.urls import path

from .views import DogView

urlpatterns = [
   path("", DogView.as_view())
]
