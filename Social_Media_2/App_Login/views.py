from django.shortcuts import render,HttpResponseRedirect
from django.urls import reverse
from App_Login.models import UserProfile,Follow
from App_Post.models import Like
from App_Login.forms import CreateNewUser,EditProfile,ChangeSettings,CreatePost
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.


def sign_up(request):

    form = CreateNewUser()

    if request.method == 'POST':

        form = CreateNewUser(data=request.POST)

        if form.is_valid():

            user = form.save()

            user_profile_page = UserProfile(user=user)
            user_profile_page.save()
            
            return HttpResponseRedirect(reverse('App_Login:login'))

    dict = {'form' : form}

    
    return render(request, 'App_Login/sign_up.html', context=dict)

def login_user(request):

    form = AuthenticationForm()

    if request.method == 'POST':

        form = AuthenticationForm(data=request.POST)

        if form.is_valid():

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:

                login(request, user)
                
                return HttpResponseRedirect(reverse('App_Post:home'))
            
    dict = {'title' : 'login', 'form' : form}

    return render(request, 'App_Login/login.html', context=dict)


@login_required
def user_profile(request):

    form = CreatePost()

    if request.method == 'POST':

        form = CreatePost(request.POST, request.FILES)

        if form.is_valid():

            form_obj = form.save(commit=False)
            form_obj.author = request.user
            form_obj.save()

            return HttpResponseRedirect(reverse('App_Post:home'))

    dict = {'title' : request.user, 'form' : form}

    return render(request, 'App_Login/profile.html', context=dict)

@login_required
def edit_user_profile(request):

    current_user = request.user

    form = EditProfile(instance=current_user.user_profile)

    if request.method == 'POST':

        form = EditProfile(request.POST, request.FILES, instance=current_user.user_profile)

        if form.is_valid():

            form_obj = form.save(commit=False)

            form_obj.user = current_user
            form_obj.save()

            return HttpResponseRedirect(reverse('App_Login:user_profile'))


    dict = {'form' : form, 'title' : request.user}

    return render(request, 'App_Login/edit_profile.html', context=dict)


def public_user_profile(request, username):

    searched_user = User.objects.get(username=username)
    current_user = request.user

    liked_post_user = Like.objects.filter(user=request.user)
    liked_post_list = liked_post_user.values_list('post', flat=True)

    already_followed = Follow.objects.filter(follower=current_user, following=searched_user)

    if already_followed:
        
        follow = False

    else:
        
        follow = True
    
    if searched_user == current_user:

        return HttpResponseRedirect(reverse('App_Login:user_profile'))

    else:

        dict = {'searched_user' : searched_user, 'follow' : follow, 'liked_post_list' : liked_post_list}
        
        return render(request, 'App_Login/public_profile.html', context=dict)

@login_required
def change_settings(request):

    current_user = request.user

    form = ChangeSettings(instance=current_user)

    if request.method == 'POST':

        form = ChangeSettings(request.POST, instance=current_user)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('App_Login:user_profile'))

    dict = {'form' : form}

    return render(request, 'App_Login/change_settings.html', context=dict)

@login_required
def change_password(request):

    current_user = request.user

    form = PasswordChangeForm(current_user)

    if request.method == 'POST':

        form = PasswordChangeForm(current_user, data=request.POST)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('App_Login:login'))


    dict = {'form' : form}

    return render(request, 'App_Login/change_password.html', context=dict)

@login_required
def follow(request, username):

    follower = request.user
    following = User.objects.get(username=username)

    already_followed = Follow.objects.filter(follower=follower, following=following)

    if not already_followed:

        followed_user = Follow(follower=follower, following=following)
        followed_user.save()

        return HttpResponseRedirect(reverse('App_Login:public_user_profile', kwargs={'username' : username}))

@login_required
def unfollow(request, username):

    follower = request.user
    following = User.objects.get(username=username)

    already_followed = Follow.objects.filter(follower=follower, following=following)
    already_followed.delete()

    return HttpResponseRedirect(reverse('App_Login:public_user_profile', kwargs={'username' : username}))



@login_required
def logout_user(request):

    logout(request)
    return HttpResponseRedirect(reverse('App_Login:login'))
    