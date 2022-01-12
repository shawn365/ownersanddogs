from django.urls import path

from .views import ActorMovieView

urlpatterns = [
    path('', ActorMovieView.as_view()),
]