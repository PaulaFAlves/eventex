from django.urls import path

from eventex.subscription.views import new, detail

app_name = 'subscription'

urlpatterns = [
    path('inscricao/', new, name='new'),
    path('inscricao/<int:pk>/', detail, name='detail'),
]