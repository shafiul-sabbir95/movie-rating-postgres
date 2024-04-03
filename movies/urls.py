from django.urls import path
from . import views
from .views import (
    MovieListView, 
    MovieDetailView,
    MovieCreateView,
    MovieUpdateView,
    MovieDeleteView,
    UserMovieListView,
)

urlpatterns = [
    path('', MovieListView.as_view(), name='movie-list'),
    path('user/<str:username>', UserMovieListView.as_view(), name='user-movies'),
    path('movie/new/', MovieCreateView.as_view(), name='movie-create'),
    path('movie/<int:pk>/', MovieDetailView.as_view(), name='movie-detail'),
    path('movie/<int:pk>/update/', MovieUpdateView.as_view(), name='movie-update'),
    path('movie/<int:pk>/delete/', MovieDeleteView.as_view(), name='movie-delete'),
    path('about/', views.about, name='about'),
    path('contact_us/', views.contact_us, name='contact-us'),
    path('contact_us_success/', views.contact_us_success, name='contact-us-success'),
]
