from django.urls import path, include
from blogging.views import BloggingListView,stub_view,BloggingDetailView

urlpatterns = [
    path('', BloggingListView.as_view(), name='blog_index'),
    path('posts/<int:pk>/', BloggingDetailView.as_view(), name='blog_detail')
]