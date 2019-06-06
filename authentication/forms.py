from django import forms


class SignUpForm(forms.Form):
    email = forms.CharField(required=True)
    password = forms.CharField()

   