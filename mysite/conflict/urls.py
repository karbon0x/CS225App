from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^signup/', views.signup, name="signup"),
    url(r'^index/', views.index, name="index"),
    url(r'^login/', views.user_login, name="login"),
    url(r'^logout/', views.user_logout, name="logout"),
]
