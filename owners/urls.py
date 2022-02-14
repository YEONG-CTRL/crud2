from django.urls import path

from owners.views import OwnersView

urlpatterns = [
    path('', OwnersView.as_view()),
]
