from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('form', views.form_view, name='form'),
    path('logger', views.logger_view, name='logger'),
    path('requestjson', views.request_json, name='requestjson'),
    path('requesttext', views.request_text, name='requesttext'),
    path('responsejson', views.response_json, name='responsejson'),

    path('dishes/<str:dish>', views.dishes, name='dishes'),
    path('menu/<str:dish>', views.menu, name='menu'),
]
