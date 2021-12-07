from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class ClientRegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(ClientRegistrationForm, self).__init__(*args, **kwargs)
        del self.fields['password2']
    email = forms.EmailField()
    class Meta:
        model = CustomUser
        fields = ['full_name','email','location','phone','is_staff']