from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CommentForm,ReplyForm
from .models import Post, Category,Comment

def detail(request, category_slug, slug):
    post = get_object_or_404(Post, slug=slug, status=Post.ACTIVE)
    

    if request.method == 'POST':
        form = CommentForm(request.POST)


        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('post_detail', category_slug=category_slug, slug=slug)
   
    else:
        form = CommentForm()


    return render(request, 'blog/detail.html', {'post': post, 'form': form})

def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = category.posts.filter(status=Post.ACTIVE)

    return render(request, 'blog/category.html', {'category': category, 'posts': posts})

def search(request):
    query = request.GET.get('query', '')

    posts = Post.objects.filter(status=Post.ACTIVE).filter(Q(title__icontains=query) | Q(intro__icontains=query) | Q(body__icontains=query))

    return render(request, 'blog/search.html', {'posts': posts, 'query': query})

def reply(request, category_slug,post_slug, comment_id):
    comment = Comment.objects.get(id=comment_id)
    post = Post.objects.get(slug=post_slug)

    if request.method == 'POST':

        formr=ReplyForm(request.POST)

        if formr.is_valid():
            reply = formr.save(commit=False)
            reply.comment = comment
            reply.save()

            return redirect('comment_detail', category_slug=category_slug,post_slug=post_slug, comment_id=comment_id)
    else:
        formr=ReplyForm()

    return render(request, 'blog/reply.html', {'post':post,'comment': comment, 'formr': formr})