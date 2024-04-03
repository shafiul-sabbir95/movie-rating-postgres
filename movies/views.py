from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Movie, Rating
from django.contrib.auth.models import User
from django.db.models import Q
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView
)

def home(request):
    context = {
        'movies': Movie.objects.all(),
        'ratings': Rating.objects.all(),
        'title': 'Home'
    }
    return render(request, 'movies/movie_list.html', context)

class MovieListView(ListView):
    model = Movie
    template_name = 'movies/movie_list.html'
    context_object_name = 'movies'
    ordering = ['-release_date']
    paginate_by = 4
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Movies'
        query = self.request.GET.get('search')
        
        if query:
            context['message'] = 'You searched for: "' + query + '". ' + 'No data found for "' + query + '"!'
        else:
            context['message'] = 'No search query provided'
        return context

    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            return Movie.objects.filter(Q(name__icontains=query))
        else:
            return Movie.objects.all()
    
class UserMovieListView(ListView):
    model = Movie
    template_name = 'movies/user_movie_list.html'
    context_object_name = 'movies'
    paginate_by = 4
    
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Movie.objects.filter(author=user).order_by('-release_date')

class MovieDetailView(DetailView):
    model = Movie
    
class MovieCreateView(LoginRequiredMixin, CreateView):
    model = Movie
    fields = ['name', 'genre', 'rating', 'release_date']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class MovieUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Movie
    fields = ['name', 'genre', 'rating', 'release_date']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        movie = self.get_object()
        if self.request.user == movie.author:
            return True
        return False

class MovieDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Movie
    success_url = '/'
    
    def test_func(self):
        movie = self.get_object()
        if self.request.user == movie.author:
            return True
        return False

def about(request):
    context = {
        'movies' : Movie.objects.all(),
        'movie_number' : Movie.objects.all().count(),
        'author_number' : Movie.objects.all().values('author').distinct().count(),
        'title' : 'About'
    }
    return render(request, 'movies/about.html', context)

def contact_us(request):
    context = {
        'title': 'Contact Us'
    }
    return render(request, 'movies/contact_us.html', context)

def contact_us_success(request):
    name = request.POST['name']
    email = request.POST['email']
    message = request.POST['message']
    context = {
        'name': name,
        'email': email,
        'message': message,
        'title': 'Contact Us'
    }
    return render(request, 'movies/contact_us_success.html', context)
