from django.shortcuts import render,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from App_Login.models import Follow
from App_Post.models import Like, Post
from .forms import CommentForm
 

# Create your views here.

@login_required
def home(request):

    user_following_list = Follow.objects.filter(follower=request.user)

    user_following_posts = Post.objects.filter(author__in=user_following_list.values_list('following')).order_by('-upload_date')

    liked_post_user = Like.objects.filter(user=request.user)
    liked_post_list = liked_post_user.values_list('post', flat=True)


    all_posts = Post.objects.all().order_by('-upload_date')

    dict = {'title' : 'home', 'user_following_list' : user_following_list , 'user_following_posts' : user_following_posts, 'all_posts' : all_posts, 'liked_post_list' : liked_post_list}

    return render(request, 'App_Post/home.html', context=dict)


@login_required
def search(request):

    if request.method == 'GET':

        search_key = request.GET.get('search', '')
        searching_value = User.objects.filter(username__icontains=search_key)


    dict = {'search_key' : search_key, 'searching_value' : searching_value}

    return render(request, 'App_Post/search.html', context=dict)



@login_required
def post_details(request,pk):

    post = Post.objects.get(pk=pk)

    liked_post_user = Like.objects.filter(user=request.user)
    liked_post_list = liked_post_user.values_list('post', flat=True)

    form = CommentForm()

    if request.method == 'POST':

        form = CommentForm(data=request.POST)

        if form.is_valid():

            form_obj = form.save(commit=False)

            form_obj.post = post
            form_obj.user = request.user
            form_obj.save()

            return HttpResponseRedirect(reverse('App_Post:post_details', kwargs={'pk' : pk}))




    dict = {'post' : post, 'form' : form, 'liked_post_list' : liked_post_list}

    return render(request, 'App_Post/post_details.html', context=dict)


@login_required
def liked(request, pk):

    post = Post.objects.get(pk=pk)
    user = request.user

    already_liked = Like.objects.filter(post=post, user=user)

    if not already_liked:

        like = Like(post=post, user=user)
        like.save()

        return HttpResponseRedirect(reverse('App_Post:home'))


@login_required
def unliked(request, pk):

    post = Post.objects.get(pk=pk)
    user = request.user

    already_liked = Like.objects.filter(post=post, user=user)
    already_liked.delete()

    return HttpResponseRedirect(reverse('App_Post:home'))


@login_required
def delete_post(request, pk):

    deleted_post = Post.objects.get(pk=pk)
    deleted_post.delete()

    return HttpResponseRedirect(reverse('App_Login:user_profile'))

