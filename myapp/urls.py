from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('requestjson', views.request_json, name='requestjson'),
    path('requesttext', views.request_text, name='requesttext'),
    path('responsejson', views.response_json, name='responsejson'),

    path('dishes/<str:dish>', views.menuitems, name='menuitems'),
]
