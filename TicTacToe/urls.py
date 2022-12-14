from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from game.views import game_view, index

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index, name="index"),
    path("games/<uuid:uuid>/", game_view, name="game_view")
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
