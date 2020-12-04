from django.urls import path
from .views import ShowBlog

urlpatterns = [
    path('', ShowBlog, name='showblog'),
]
