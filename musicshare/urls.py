from django.urls import path
from . import views
from . import settings
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from django.conf.urls.static import static
urlpatterns = [
    path('',PostListView.as_view(),name='music-home'),
    path('post/new/',PostCreateView.as_view(),name='music-create'),
    path('post/<int:pk>/',PostDetailView.as_view(),name='music-detail'),
    path('post/<int:pk>/update',PostUpdateView.as_view(),name='music-update'),
    path('post/<int:pk>/delete',PostDeleteView.as_view(),name='music-delete'),
    path('about/',views.about,name='music-about'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
