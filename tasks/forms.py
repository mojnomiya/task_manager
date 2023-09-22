from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class UserRegForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        placeholders = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'username': 'Username',
            'email': 'Email',
            'password1': 'Password',
            'password2': 'Confirm Password'
        }
        
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'placeholder': placeholders.get(field)
            })
        
        self.fields['first_name'].widget.attrs['autofocus'] = True

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
        placeholders = {
            'username': 'Username',
            'password': 'Password',
        }

        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'placeholder': placeholders.get(field)
            })