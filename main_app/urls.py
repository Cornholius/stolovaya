from django.urls import path
from . import views
#   добавляем для работы медиа файлов при отключенном дебаге
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', )
]