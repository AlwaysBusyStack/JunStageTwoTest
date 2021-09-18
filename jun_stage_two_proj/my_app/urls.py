from django.urls import path, include
from django.contrib.auth import logout

from my_app.views import (
    get_authentificated_view,
    logout_from_app,
)

urlpatterns = [
    path('', get_authentificated_view),
    path('logout/', logout_from_app),
]
