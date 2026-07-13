from django.urls import path

from . import views

# All 8 URL patterns for the blog app
urlpatterns = [
    # Homepage — list of all published posts
    path('', views.HomeView.as_view(), name='home'),

    # Single post detail
    path('post/<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),

    # Create a new post (requires login)
    path('post/new/', views.PostCreateView.as_view(), name='post_create'),

    # Edit an existing post (author only)
    path('post/<slug:slug>/edit/', views.PostUpdateView.as_view(), name='post_edit'),

    # Delete a post (author only)
    path('post/<slug:slug>/delete/', views.PostDeleteView.as_view(), name='post_delete'),

    # User registration
    path('register/', views.register_view, name='register'),

    # Add a comment to a post
    path('post/<slug:slug>/comment/', views.add_comment, name='add_comment'),

    # Posts by category
    path('category/<slug:slug>/',
         views.CategoryPostsView.as_view(),
         name='category_posts'),
]
