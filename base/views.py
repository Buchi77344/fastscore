from django.shortcuts import render, get_object_or_404
from .models import Post



def index(request):
    return render (request, 'index.html') 

def base(request):
    cap = Post.objects.all()
    context = {
        'cap':cap
    }
    return render (request,'base.html',context)
def post_de(request , slug):
    pos = get_object_or_404 (Post, slug=slug)
    pob = Post.objects.all()
    context = {
        'pos':pos,
        'pob':pob
    }
    return render (request, 'post_de.html',context)
