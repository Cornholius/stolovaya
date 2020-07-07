from django.urls import path
from . import views


urlpatterns = [
    path('', views.MainPage.as_view(), name='main'),
    path('menu/<menu_type>', views.Menu.as_view(), name='menulist'),
    path('business_lunch/', views.TodayInMenu.as_view(), name='menutoday'),
]
