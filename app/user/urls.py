"""
URL mappings for the user API
"""
from django.urls import path
from user.views import (
    CreateUserView,
    CreateTokenView,
    MangeUserView
)


app_name = 'user'

urlpatterns = [
    path('create/', CreateUserView.as_view(), name='create'),
    path('token/', CreateTokenView.as_view(), name='token'),
    path('me/', MangeUserView.as_view(), name='me'),
]

