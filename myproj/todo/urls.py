from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^see_tasks$', views.see_tasks, name='see_tasks'),
    url(r'^create$', views.create, name='create'),

]
