from django.urls import path

from .views import OwnerView

urlpatterns = [
    path("", OwnerView.as_view())
]
