from django.urls import path

from eventex.subscription.views import subscribe, detail

urlpatterns = [
    path('inscricao/', subscribe),
    path('inscricao/<int:pk>/', detail),
]