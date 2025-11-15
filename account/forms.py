from django import forms
from django.contrib.auth.models import User
from .models import Profile
class edituserform(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','email',)

