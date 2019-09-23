from django.urls import path
from . import views

urlpatterns = [
    path('index',views.make_a_call,name='urls_tested')
]
