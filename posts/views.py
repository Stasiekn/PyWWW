from django.http import HttpResponse
from posts.models import Post
from django.template import loader
from django.shortcuts import render
from django.contrib.auth.models import AnonymousUser
from posts.forms import PostForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from posts.models import Post


def add_post_form(request):
    if request.method == "POST" and request.user.is_authenticated:
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return HttpResponseRedirect(reverse("posts:add"))
    else:
        form = PostForm()
    return render(request, "posts/add.html", {"form": form})


def post_list(request):
    posts = Post.objects.filter(published=True)
    q = request.GET.get("q")
    if q:
        post = posts.filter(title__icontains=q)
    context = {'posts_list' : posts}
    return render(request, "posts/list.html", context)


def post_details(request, post_id: int):
    post = Post.objects.get(pk=post_id)
    context ={}
    if post.published:
        context["post"] = post
    return render(request, "posts/details.html", context)


def edit_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
    else:
        form = PostForm(instance=post)

    return render(request, "posts/add.html", {"form" : form})






