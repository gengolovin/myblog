from django.urls import path
from .views import ShowBlog, post_details

urlpatterns = [
    path('', ShowBlog, name='showblog'),
    path('<int:post_id>/', post_details, name='post_details'),
]
