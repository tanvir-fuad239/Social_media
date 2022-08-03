from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from App_Login.models import UserProfile
from App_Post.models import Post

class CreateNewUser(UserCreationForm):

    email = forms.EmailField(label="", widget=forms.TextInput(attrs={
        "placeholder" : "email", "style" : "font-style: italic; padding: 8px; margin-bottom: 15px;"

    }))

    username = forms.CharField(label="", widget=forms.TextInput(attrs={
        "placeholder" : "username", "style" : "font-style: italic; padding: 8px; margin-bottom: 15px;"

    }))
    
    password1 = forms.CharField(label="", widget=forms.PasswordInput(attrs={
        "placeholder" : "password", "style" : "font-style: italic; padding: 8px; margin-bottom: 15px;"
 
    }))

    password2 = forms.CharField(label="", widget=forms.PasswordInput(attrs={
        "placeholder" : "password conformation", "style" : "font-style: italic; padding: 8px; margin-bottom: 15px;"
 
    }))

    class Meta:

        model = User
        fields = ('email', 'username', 'password1', 'password2')




class EditProfile(forms.ModelForm):

    date_of_birth = forms.CharField(widget=forms.TextInput(attrs={
        'type' : 'date'
    }))

    class Meta:

        model = UserProfile
        exclude = ['user', ]



class ChangeSettings(UserChangeForm):
    class Meta:

        model = User
        fields = ('email','username','password')



class CreatePost(forms.ModelForm):

    post_image = forms.ImageField(required=True)

    class Meta:

        model = Post
        fields = ('post_image', 'caption')