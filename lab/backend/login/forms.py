from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    full_name = forms.CharField(
        max_length=100, 
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your Full Name', 'class': 'name'})
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Enter your Email', 'class': 'email'})
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter your Username', 'class': 'username'})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'password'})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 'class': 'cPassword'})
    )

    class Meta:
        model = User
        fields = ('full_name', 'username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        full_name = self.cleaned_data['full_name']
        if full_name:
            user.first_name = full_name.split()[0]
            user.last_name = ' '.join(full_name.split()[1:])
        if commit:
            user.save()
        return user
