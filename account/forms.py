from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError

class CustomUserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email']
        
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError("The username already exists")
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("The email already exists")
        return email
    
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        username = self.cleaned_data.get('username')
        
        if password1 and password2 and password1 != password2:
            raise ValidationError("Password do not match")
        if username and username.lower() in password1.lower():
            raise ValidationError("Password cannot contain username")
        return password2
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user