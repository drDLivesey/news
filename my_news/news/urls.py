from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('^tag/(?P<tag_slug>[-\w]+)/$', views.home, name='home_tag'),
    path('<int:id>/', views.single, name='single'),
]