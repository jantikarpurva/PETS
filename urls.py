from django.conf.urls import url,include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^petApp/$', views.index),
    url(r'^dog-form/', views.dogForm),
    url(r'^cat-form/', views.catForm),
    url(r'^rabit-form/', views.rabbitForm),
    url(r'^hamster-form/', views.hamsterForm),
    url(r'^login/', views.login_user),
    url(r'^logout/', views.logout_user),
    url(r'^dog-detail/', views.dogDetail),
    url(r'^cat-detail', views.catDetail),
    url(r'^rabbit-detail', views.rabbitDetail),
    url(r'^hamster-detail', views.hamsterDetail),
    url(r'^index-login/', views.indexLogin),
    url(r'^index-logout/', views.indexLogout),
    url(r'^view-dog/', views.viewDog),
    url(r'^view-cat/', views.viewCat),
    url(r'^view-rabbit/', views.viewRabbit),
    url(r'^view-hamster/', views.viewHamster),
    url(r'^blog/', views.blog),
]