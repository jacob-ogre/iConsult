from django import forms
from django.db import models
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Consultation

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Provide a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )

class UserForm(forms.ModelForm):
    class Meta:
        model = User 
        fields = ["first_name", "last_name", "email"]

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

class ConsultForm(forms.ModelForm):
    class Meta:
        model = Consultation
        DATUM_OPTS = (
            ("NAD27", "NAD27"),
            ("NAD83", "NAD83"),
            ("WGS84", "WGS84"),
        )
        datum = forms.ChoiceField(choices=DATUM_OPTS)    
        fields = ("title", "summary", "location", "lat", "long", "datum",
            "species", "area", "area_unit", "owner", "date_created", 
            "date_modified")
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "Descriptive is better"}),
            "location": forms.TextInput(attrs={"placeholder": "Placenames, Township/Sect/Range,etc"}),
            "summary": forms.Textarea(attrs={"placeholder": "The action, anticipated effects, etc., in prose"}),
            "species": forms.TextInput(attrs={"placeholder": "Semicolon-separated list"}),
            "area_unit": forms.TextInput(attrs={"placeholder": "e.g., acres"}),
            "lat": forms.TextInput(attrs={"placeholder": "decimal degrees"}),
        }