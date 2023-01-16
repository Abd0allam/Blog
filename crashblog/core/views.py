from django.http.response import HttpResponse
from django.http import HttpResponse
from django.shortcuts import render ,redirect
from blog.models import Post
from django.contrib.auth import login
from .forms import SignUpForm

def frontpage(request):
    posts = Post.objects.filter(status=Post.ACTIVE)

    return render(request, 'core/frontpage.html', {'posts': posts})

def about(request):
    return render(request, 'core/about.html')

def robots_txt(request):
    text = [
        "User-Agent: *",
        "Disallow: /admin/",
    ]
    return HttpResponse("\n".join(text), content_type="text/plain")

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('frontpage')
    else:
        form = SignUpForm()
    
    return render(request, 'core/signup.html', {'form': form})