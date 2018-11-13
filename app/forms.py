from django import forms
from django.core.exceptions import ValidationError                          # Validation Error method 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm      # Using django's predefined forms
from .models import user, Village,SHG

# Form for creating new user 
class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User                                        # using the user model
        fields = ('username', 'is_village','is_shg')
        help_texts = {'username':(''),}

# Form to change information of existing user    	    	
class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('is_village','is_shg',)

