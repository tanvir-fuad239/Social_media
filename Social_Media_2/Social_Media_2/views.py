from django.shortcuts import HttpResponseRedirect
from django.urls import reverse


def index(request):

    if request.user.is_authenticated:

        return HttpResponseRedirect(reverse('App_Post:home'))

    else:

        return HttpResponseRedirect(reverse('App_Login:login'))
