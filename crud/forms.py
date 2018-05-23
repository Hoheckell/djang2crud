from django import forms
from crud.models import User

class UserForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email',max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    confirm = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class UpdUserForm(forms.ModelForm):
    class Meta:
       model = User
       fields = ['nome','email']
    # nome = forms.CharField(label='Nome', max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    #email = forms.EmailField(label='Email',max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
