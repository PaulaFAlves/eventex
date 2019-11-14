from django.urls import path

from eventex.subscription.views import subscribe, detail

app_name = 'subscription'

urlpatterns = [
    path('inscricao/', subscribe, name='new'),
    path('inscricao/<int:pk>/', detail, name='detail'),
]