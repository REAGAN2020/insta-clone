from django.shortcuts import render, redirect, get_object_or_404
from .models import Image, Profile, Comment, Relation
from django.contrib.auth.models import User

# Create your views here.
def feed(request):
    pictures = Image.objects.all()
    number = Comment.objects.count()
    return render(request, 'index.html', {'pictures': pictures, 'number': number})

def profile(request):
    current_user = request.user.profile
    pics = Image.objects.filter(profile=current_user).all()
    return render(request, 'profile.html', {'pics':pics})
