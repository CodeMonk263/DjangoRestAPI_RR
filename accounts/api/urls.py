from django.conf.urls import url, include
from django.contrib import admin

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from .views import AuthenticationAPIView, RegisterAPIView

urlpatterns = [
    url(r'^login/$', AuthenticationAPIView.as_view()),
    url(r'^refresh/$', refresh_jwt_token),
    url(r'^register/$', RegisterAPIView.as_view()),
]
