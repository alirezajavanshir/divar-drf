from django.contrib import admin
from django.urls import path, include
from chat import routing


urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("listings/", include("listings.urls")),
    path("chat/", include(routing.websocket_urlpatterns)),
]
