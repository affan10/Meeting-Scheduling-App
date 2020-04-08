from django.urls import path
from . import views

app_name = 'meetings'
urlpatterns = [
    path('<int:id>', views.detail, name='detail'),
    path('rooms', views.rooms_list, name='rooms-list'),
    path('new', views.new, name='new'),
]