from django.urls import path
from . import views
#   добавляем для работы медиа файлов при отключенном дебаге
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.MainPage.as_view(), name='main'),
    path('menu/<menu_type>', views.Menu.as_view(), name='menulist')
]
