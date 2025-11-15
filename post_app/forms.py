from django import forms
from django.core.validators import ValidationError
from fastapi.openapi.models import Contact

from post_app.models import messagecontactus


# class Contactusform(forms.Form):
#     email=forms.EmailField(label='Email',required=True)
#     subject=forms.CharField(max_length=50,label="Subject",required=True)
#     message=forms.CharField(max_length=500,label="Message",required=True)
#
#     def clean(self):
#         email=self.cleaned_data.get('email')
#         subject=self.cleaned_data.get('subject')
#         message=self.cleaned_data.get('message')
#         if subject==message:
#             raise ValidationError("subject and message are same",code="name_text")
#
#
class Contactusform(forms.ModelForm):
    class Meta:
        model = messagecontactus
        fields = ("subject","message")

        widgets={
            "subject":forms.TextInput(attrs={'class':'form-control','placeholder':'Subject of your message'}),
        }
