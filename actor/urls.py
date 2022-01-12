from django.urls import path

from .views import ActorView

urlpatterns = [
    path("", ActorView.as_view())
]
