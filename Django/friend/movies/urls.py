from django.urls import path, include
from . import views
# 얘는 현재 폴더에서 views를 들고오는거

app_name = 'movies'


urlpatterns = [
    path('details/', views.details, name='details')
]
