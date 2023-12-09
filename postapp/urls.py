from django.urls import path
# from . import views
from .views import PostListView, PostDetailView, PostDeleteView, PostCreateView


urlpatterns = [
    path('posts/', PostListView.as_view(), name='posts'),
    path('post/<str:pk>', PostDetailView.as_view(), name='post'),
    path('post/delete/<str:pk>', PostDeleteView.as_view(), name='postdelete'),
    path('post/create/', PostCreateView.as_view(), name='createpost'),
    # path('post/<str:pk>', views.post, name="post"),
    # path('postdelete/<str:pk>', views.postdelete, name='postdelete'),
    # path('postupdate/<str:pk>', views.updatepost, name='postupdate'),
]