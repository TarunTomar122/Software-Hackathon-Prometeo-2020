from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class DoctorSignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        verified = False
        if commit:
            user.save()
        return user

class DoctorDetailForm(forms.ModelForm):
    class Meta:
        model = User

        fields = [
            "username",
            "first_name",
            "last_name",
            "image",
            "degree",
            "about",
            "certificate",
        ]        