from django import forms
from .models import Contact

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
