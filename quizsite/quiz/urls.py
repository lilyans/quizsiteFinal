from django.urls import path, re_path, register_converter
from . import views
from .views import ContactCreate, quiz_view


urlpatterns = [
    path('', views.index, name="index"),
    path('send_question', ContactCreate.as_view(), name='contact_form'),
    path('<str:subject>/', quiz_view, name='quiz')
]
