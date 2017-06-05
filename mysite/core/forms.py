from django import forms
from django.db import models
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# from uploads.core.models import Document

# from multiupload.fields import MultiFileField

# from django_markdown.fields import MarkdownFormField
# from django_markdown.widgets import MarkdownWidget

from .models import Consultation

class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        max_length=254,
        help_text='Required. Provide a valid email address.'
    )

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
        biop = forms.FileField(
            label="Select a file",
            help_text="5MB max."
        )
        fields = ("title", "summary", "location", "lat", "long", "datum",
            "species", "area", "area_unit", "biop",
            "owner", "date_created",
            "date_modified")
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "Descriptive is better"}),
            "location": forms.TextInput(attrs={"placeholder": "Placenames, Township/Sect/Range,etc"}),
            "species": forms.TextInput(attrs={"placeholder": "Semicolon-separated list"}),
            "area_unit": forms.TextInput(attrs={"placeholder": "e.g., acres"}),
            "lat": forms.TextInput(attrs={"placeholder": "decimal degrees"}),
            "long": forms.TextInput(attrs={"placeholder": "decimal degrees"}),
        }
