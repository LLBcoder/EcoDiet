from django import forms 
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RestrictionsForm(forms.ModelForm):
    class Meta:
        model = Restrictions
        fields = ['intolerance', 'ingredient']

    intolerance = forms.ModelMultipleChoiceField(
        queryset=Intolerances.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    ingredient = forms.ModelMultipleChoiceField(
        queryset=Ingredients.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )



class DietForm(forms.ModelForm):
    class Meta:
        model = Restrictions
        fields = ['currentdiet', 'dietgoal', 'level', 'intolerance', 'ingredient']

        widgets = {
            'currentdiet' : forms.Select(attrs={'class': 'form-select field'}),
            'dietgoal' : forms.Select(attrs={'class' : 'form-select field'}),                    
            'level' : forms.Select(attrs={'class' : 'form-select field2'}),                     
        } 

    intolerance = forms.ModelMultipleChoiceField(
        queryset=Intolerances.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    ingredient = forms.ModelMultipleChoiceField(
        queryset=Ingredients.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )


class CreateUserForm(UserCreationForm):
    class Meta :
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        widgets = {
                'username' : forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}),
                'email' : forms.TextInput(attrs={'placeholder': 'Email', 'class' : 'form-control'}),                    
                } 

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={'placeholder': 'Password','class': 'form-control'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'placeholder': 'Confirm your password','class': 'form-control'})
        