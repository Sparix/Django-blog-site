from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import *


class AddPostForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = 'Categories is not required'

    class Meta:
        model = Car
        fields = ['name', 'slug', 'content', 'photo', 'is_published', 'cat']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            'slug': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'class': 'text-area'}),
            'photo': forms.FileInput(attrs={'class': 'image-form'}),
            'is_published': forms.CheckboxInput(attrs={'class': 'published-form'}),
            'cat': forms.Select(attrs={'class': 'choice-select'})
        }


'''class AddPostForm(forms.Form):
    name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-input'}))
    slug = forms.SlugField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-input'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'text-area'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'image-form'}))
    is_published = forms.BooleanField(required=False, initial=True,
                                      widget=forms.CheckboxInput(attrs={'class': 'published-form'}))
    cat = forms.ModelChoiceField(queryset=Categories.objects.all(),
                                 widget=forms.NullBooleanSelect(attrs={'class': 'choice-select'}))'''


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input'}))
