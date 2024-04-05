from django import forms
from .models import Rating, Movie

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['user', 'movie', 'rating']
        
class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['name', 'genre', 'rating', 'release_date']  # Adjusted fields to match the model
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter movie name'}),
            'genre': forms.TextInput(attrs={'placeholder': 'Enter genre'}),
            'rating': forms.TextInput(attrs={'placeholder': 'Enter rating'}),
            'release_date': forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD'}),
        }
        error_messages = {
            'release_date': {
                'invalid': "Please enter a valid date in the format YYYY-MM-DD.",
            }
        }