from django.urls import path
from .views import   index, detailOwn

urlpatterns = [
    path('', index, name='index'),
    path('<str:id>/', detailOwn, name="detailOwn")
]
