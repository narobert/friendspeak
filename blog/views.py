# Create your views here.
from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.utils import timezone
from django import forms
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from blog.forms import UserForm, WPostForm, PPostForm, WCommentForm, PCommentForm
from blog.models import Wpost, Ppost, Profile, Wcomment, Pcomment, Wlike, Wdislike, Plike, Pdislike
from annoying.decorators import ajax_request
import simplejson as json


def home(request):
    total = 0
    wallposts = Wpost.objects.all().order_by("-id")
    wallcomments = Wcomment.objects.all().order_by("-id")
    friends = User.objects.all()
    needclick = Ppost.objects.filter(user2 = request.user.id, clicked = False).order_by("-id")
    allposts = Ppost.objects.filter(user2 = request.user.id).order_by("-id")
    for n in needclick:
        total = total + 1
    if not request.user.is_authenticated():
        return render_to_response("register.html")
    return render_to_response("home.html", {"user": request.user, "friends": friends, "wallposts": wallposts, "allposts": allposts, "total": total, "wallcomments": wallcomments})



def click(request, id):
    total = 0
    friends = User.objects.all()
    profileposts = Ppost.objects.get(id = id)
    profileposts.clicked = True
    profileposts.save()
    like = Plike.objects.get(user = request.user.id, profile = profileposts)
    dislike = Pdislike.objects.get(user = request.user.id, profile = profileposts)
    profilecomments = Pcomment.objects.filter(profile = profileposts).order_by("-id")
    needclick = Ppost.objects.filter(user2 = request.user.id, clicked = False).order_by("-id")
    allposts = Ppost.objects.filter(user2 = request.user.id).order_by("-id")
    for n in needclick:
        total = total + 1
    if not request.user.is_authenticated():
        return render_to_response("register.html")
    return render_to_response("click.html", {"user": request.user, "friends": friends, "profileposts": profileposts, "profilecomments": profilecomments, "allposts": allposts, "like": like, "dislike": dislike, "total": total})


def myprofile(request):
    total = 0
    friends = User.objects.all()
    profileposts = Ppost.objects.filter(user2 = request.user.id).order_by("-id")
    profilecomments = Pcomment.objects.filter(profile = profileposts).order_by("-id")
    needclick = Ppost.objects.filter(user2 = request.user.id, clicked = False).order_by("-id")
    allposts = Ppost.objects.filter(user2 = request.user.id).order_by("-id")
    for n in needclick:
        total = total + 1
    if not request.user.is_authenticated():
        return render_to_response("register.html")
    return render_to_response("myprofile.html", {"user": request.user, "friends": friends, "profileposts": profileposts, "profilecomments": profilecomments, "allposts": allposts, "total": total})


def profile(request, username):
    total = 0
    if (Profile.objects.filter(user__username = username).count() == 0):
        return render_to_response("error.html")
    friends = User.objects.all()
    profileposts = Ppost.objects.filter(user2__username = username).order_by("-id")
    profilecomments = Pcomment.objects.filter(profile = profileposts).order_by("-id")
    needclick = Ppost.objects.filter(user2 = request.user.id, clicked = False).order_by("-id")
    allposts = Ppost.objects.filter(user2 = request.user.id).order_by("-id")
    for n in needclick:
        total = total + 1
    if not request.user.is_authenticated():
        return render_to_response("register.html")
    return render_to_response("profile.html", {"user": request.user, "friends": friends, "username": username, "profileposts": profileposts, "profilecomments": profilecomments, "allposts": allposts, "total": total})


def postwall(request):
    if request.method == 'POST':
        form = WPostForm(request.POST)
        if form.is_valid():
            wallpost = form.cleaned_data['wallpost']
            createpost = Wpost.objects.create(user = request.user, wallpost = wallpost)
            createpost.save()
            for u in User.objects.all():
                createlike = Wlike.objects.create(user = u, wall = createpost)
                createdislike = Wdislike.objects.create(user = u, wall = createpost)
                createlike.save()
                createdislike.save()
            return HttpResponseRedirect('/')
    else:
        form = WPostForm()
    return render_to_response("error.html", {"form": form})


def commentwall(request, id):
    if request.method == 'POST':
        form = WCommentForm(request.POST)
        if form.is_valid():
            wallpost = Wpost.objects.get(id = id)
            if wallpost.hascomments == False:
                wallpost.hascomments = True
                wallpost.save()
            wallcomment = form.cleaned_data['wallcomment']
            createcomment = Wcomment.objects.create(user = request.user, wallcomment = wallcomment, wall = wallpost)
            createcomment.save()
            return HttpResponseRedirect('/')
    else:
        form = WCommentForm()
    return render_to_response("error.html", {"form": form})


@ajax_request
def getCommentsW(request):
    id = request.POST.get("id")
    wallpost = Wpost.objects.get(id=id)

    comments = Wcomment.objects.filter(wall = wallpost).order_by("-id")
    wallcomments = [pl.for_json() for pl in comments]

    return {"status": "OK", "wallcomments": wallcomments}


@ajax_request
def likewall(request, id):
    wallpost = Wpost.objects.get(id = id)
    walllike = Wlike.objects.get(user = request.user, wall = wallpost)
    walldislike = Wdislike.objects.get(user = request.user, wall = wallpost)

    if walllike.color == 0 and walldislike.color == 10:
        wallpost.likes += 1
        wallpost.save()
        walllike.color = 1
        walllike.save()

    elif walllike.color == 1 and walldislike.color == 10:
        wallpost.likes -= 1
        wallpost.save()
        walllike.color = 0
        walllike.save()

    elif walllike.color == 0 and walldislike.color == 11:
        wallpost.likes += 2
        wallpost.save()
        walldislike.color = 10
        walllike.color = 1
        walldislike.save()
        walllike.save()

    return HttpResponseRedirect('/')


@ajax_request
def dislikewall(request, id):
    wallpost = Wpost.objects.get(id = id)
    walldislike = Wdislike.objects.get(user = request.user, wall = wallpost)
    walllike = Wlike.objects.get(user = request.user, wall = wallpost)

    if walldislike.color == 10 and walllike.color == 0:
        wallpost.likes -= 1
        wallpost.save()
        walldislike.color = 11
        walldislike.save()

    elif walldislike.color == 11 and walllike.color == 0:
        wallpost.likes += 1
        wallpost.save()
        walldislike.color = 10
        walldislike.save()

    elif walldislike.color == 10 and walllike.color == 1:
        wallpost.likes -= 2
        wallpost.save()
        walllike.color = 0
        walldislike.color = 11
        walllike.save()
        walldislike.save()

    return HttpResponseRedirect('/')


@ajax_request
def getLikesW(request):
    wallpost = Wpost.objects.all().order_by("-id")
    walllikes = [pl.for_json() for pl in wallpost]

    return {"status": "OK", "walllikes": walllikes}


@ajax_request
def getLikeW(request):
    wlike = Wlike.objects.filter(user = request.user)
    walllike = [pl.for_json() for pl in wlike]

    return {"status": "OK", "walllike": walllike}


@ajax_request
def getDislikeW(request):
    wdislike = Wdislike.objects.filter(user = request.user)
    walldislike = [pl.for_json() for pl in wdislike]

    return {"status": "OK", "walldislike": walldislike}


def postprofile(request, username):
    if request.method == 'POST':
        form = PPostForm(request.POST)
        if form.is_valid():
            profilepost = form.cleaned_data['profilepost']
            profile = Profile.objects.get(user__username = username)
            createpost = Ppost.objects.create(user1 = request.user, user2 = profile.user, profilepost = profilepost)
            createpost.save()
            for u in User.objects.all():
                createlike = Plike.objects.create(user = u, profile = createpost)
                createdislike = Pdislike.objects.create(user = u, profile = createpost)
                createlike.save()
                createdislike.save()
            return HttpResponseRedirect('/profile/' + username + '/')
    else:
        form = PPostForm()
    return render_to_response("error.html", {"form": form})


def commentprofile(request, id):
    if request.method == 'POST':
        form = PCommentForm(request.POST)
        if form.is_valid():
            profilepost = Ppost.objects.get(id = id)
            if profilepost.hascomments == False:
                profilepost.hascomments = True
                profilepost.save()
            profilecomment = form.cleaned_data['profilecomment']
            createcomment = Pcomment.objects.create(user = request.user, profilecomment = profilecomment, profile = profilepost)
            createcomment.save()
            url = reverse('profile', kwargs={'username': profilepost.user2.username})
            return HttpResponseRedirect(url)
    else:
        form = PCommentForm()
    return render_to_response("error.html", {"form": form})


def commentpost(request, id):
    if request.method == 'POST':
        form = PCommentForm(request.POST)
        if form.is_valid():
            profilepost = Ppost.objects.get(id = id)
            if profilepost.hascomments == False:
                profilepost.hascomments = True
                profilepost.save()
            profilecomment = form.cleaned_data['profilecomment']
            createcomment = Pcomment.objects.create(user = request.user, profilecomment = profilecomment, profile = profilepost)
            createcomment.save()
            url = reverse('click', kwargs={'id': id})
            return HttpResponseRedirect(url)
    else:
        form = PCommentForm()
    return render_to_response("error.html", {"form": form})


@ajax_request
def getCommentsP(request):
    id = request.POST.get("id")
    profilepost = Ppost.objects.get(id=id)

    comments = Pcomment.objects.filter(profile = profilepost).order_by("-id")
    profilecomments = [pl.for_json() for pl in comments]

    return {"status": "OK", "profilecomments": profilecomments}


@ajax_request
def likeprofile(request, id):
    profilepost = Ppost.objects.get(id = id)
    profilelike = Plike.objects.get(user = request.user, profile = profilepost)
    profiledislike = Pdislike.objects.get(user = request.user, profile = profilepost)

    if profilelike.color == 0 and profiledislike.color == 10:
        profilepost.likes += 1
        profilepost.save()
        profilelike.color = 1
        profilelike.save()

    elif profilelike.color == 1 and profiledislike.color == 10:
        profilepost.likes -= 1
        profilepost.save()
        profilelike.color = 0
        profilelike.save()

    elif profilelike.color == 0 and profiledislike.color == 11:
        profilepost.likes += 2
        profilepost.save()
        profiledislike.color = 10
        profilelike.color = 1
        profiledislike.save()
        profilelike.save()

    url = reverse('click', kwargs={'id': id})
    return HttpResponseRedirect(url)


@ajax_request
def dislikeprofile(request, id):
    profilepost = Ppost.objects.get(id = id)
    profiledislike = Pdislike.objects.get(user = request.user, profile = profilepost)
    profilelike = Plike.objects.get(user = request.user, profile = profilepost)

    if profiledislike.color == 10 and profilelike.color == 0:
        profilepost.likes -= 1
        profilepost.save()
        profiledislike.color = 11
        profiledislike.save()

    elif profiledislike.color == 11 and profilelike.color == 0:
        profilepost.likes += 1
        profilepost.save()
        profiledislike.color = 10
        profiledislike.save()

    elif profiledislike.color == 10 and profilelike.color == 1:
        profilepost.likes -= 2
        profilepost.save()
        profilelike.color = 0
        profiledislike.color = 11
        profilelike.save()
        profiledislike.save()

    url = reverse('click', kwargs={'id': id})
    return HttpResponseRedirect(url)


@ajax_request
def getLikesP(request):
    profilepost = Ppost.objects.all().order_by("-id")
    profilelikes = [pl.for_json() for pl in profilepost]

    return {"status": "OK", "profilelikes": profilelikes}


@ajax_request
def getLikeP(request):
    plike = Plike.objects.filter(user = request.user)
    profilelike = [pl.for_json() for pl in plike]

    return {"status": "OK", "profilelike": profilelike}


@ajax_request
def getDislikeP(request):
    pdislike = Pdislike.objects.filter(user = request.user)
    profiledislike = [pl.for_json() for pl in pdislike]

    return {"status": "OK", "profiledislike": profiledislike}


def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['username']
            pw = form.cleaned_data['password']
            newuser = User.objects.create_user(name, form.cleaned_data['email'], pw)
            newuser.save()
            profile = Profile.objects.create(user = newuser)
            profile.save()
            user = authenticate(username = name, password = pw)
            auth_login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = UserForm()
    return render_to_response("register.html", {'form':form})


def login(request):
    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
  
        user = authenticate(username = username, password = password)
        if user is not None:
            auth_login(request, user)
            return HttpResponseRedirect('/')
        else:
            newuser = User.objects.create_user(username = username, email = 'testemail@ucsd.edu', password = password)
            newuser.save()
            user = authenticate(username = username, password = password)
            auth_login(request, user)
            return redirect("afterlogin")
    return render_to_response("login.html")


def afterlogin(request):
    profilename = profilelocale = profileage = ''
    if request.POST:
        profilename = request.POST.get('profilename')
        profilelocale = request.POST.get('profilelocale')
        profileage = request.POST.get('profileage')
        profile = Profile.objects.create(user = request.user, name = profilename, locale = profilelocale, age = profileage)
        profile.save()
        return HttpResponseRedirect('/')
    return render_to_response("login.html")
  

def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('/')
