from django.urls import path
from .views import HomeBlogPage, BlogDetailView, BlogCreatePost
urlpatterns = [
    path('home/', HomeBlogPage.as_view(),name = 'blog_home'),
    path('detail_view/<int:pk>/',BlogDetailView.as_view(), name ='detail_view'),
    path('post/new/', BlogCreatePost.as_view(), name='new_post'),

]




