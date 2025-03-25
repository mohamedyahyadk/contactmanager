from django import forms
from .models import Contact 
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm ,UsernameField

User=get_user_model()


class UserCreationForm(UserCreationForm):
      class Meta:
         model=User
         fields=["username"]
         field_classes={"username":UsernameField}





class ContactModelForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields=(
            'name',
            'email',
            'phone',
            'registrar',
        )

# class ContactForm(forms.Form):
#     name=forms.CharField()
#     email=forms.EmailField()
#     phone=forms.IntegerField()
