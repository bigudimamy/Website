from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import Products, CategoryProducts
from django.forms import ModelForm, TextInput, FileInput, NumberInput, Textarea, ModelChoiceField, PasswordInput, EmailInput

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        email = forms.EmailField()
        model = User
        fields = ['username', 'password1', 'password2', 'email']

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

class ProductsForm(ModelForm):
    category = ModelChoiceField(queryset=CategoryProducts.objects.all(), empty_label="Выберите категорию",
                                label="Категория", widget=forms.Select(attrs={'class': 'form-control'}))
    class Meta:
        model = Products
        fields = ['name_product', 'description', 'price', 'quantity', 'image', 'category']

        widgets = {
            "name_product": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название'
            }),
            "description": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание'
            }),
            "price": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Цена'
            }),
            "quantity": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Количество'
            }),
            "image": FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фото'
            }),
        }