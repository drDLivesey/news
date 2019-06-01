from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('<int:id>/', views.single, name='single'),
    path('tag/'+'<str:tag>', views.tags_list, name='tags_list_url'),
]