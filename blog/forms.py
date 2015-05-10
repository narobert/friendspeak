from django import forms
from django.forms.widgets import PasswordInput
from django.contrib.auth.models import User
	
class UserForm(forms.Form):
    username = forms.CharField(max_length = 20)
    password = forms.CharField(widget = PasswordInput, max_length = 40)
    email = forms.EmailField()
	
    def clean_username(self):
        try:
            User.objects.get(username = self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError('Username taken.')

class WPostForm(forms.Form):
    wallpost = forms.CharField(max_length = 1000)

class PPostForm(forms.Form):
    profilepost = forms.CharField(max_length = 1000)

class WCommentForm(forms.Form):
    wallcomment = forms.CharField(max_length = 500)

class PCommentForm(forms.Form):
    profilecomment = forms.CharField(max_length = 500)
