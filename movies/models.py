from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Movie(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    rating = models.CharField(max_length=5)
    release_date = models.DateField()
    date_posted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('movie-detail', kwargs={'pk': self.pk})

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='ratings')
    rating = models.DecimalField(max_digits=3, decimal_places=1)

    class Meta:
        unique_together = ('user', 'movie')

    def __str__(self):
        return f'{self.user.username} - {self.movie.name} - {self.rating}'
