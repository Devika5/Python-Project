from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model=Movie
        fields=['name','desc','year','img']

# from django import forms
# from .models import Movie
#
# class MovieForm(forms.ModelForm):
#     class Meta:
#         model = Movie  # Specify the associated model class
#         fields = ['name', 'desc', 'year', 'img']