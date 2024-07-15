from django.shortcuts import render,redirect
from .models import Post
from .forms import PostForm

# Create your views here.

def main(req):
  posts = Post.objects.all()
  search_txt = req.GET.get('search_txt')
  max_price = req.GET.get('max_price')
  min_price = req.GET.get('min_price')

  if search_txt:
    posts = posts.filter(title__contains = search_txt)
  if max_price:
    posts = posts.filter(price__lt = max_price)
  if min_price:
    posts = posts.filter(price__gt = min_price)
  ctx = {'posts': posts}
  return render(req,'posts/list.html',ctx)

def create(req):
  if req.method == "GET":
    form = PostForm()
    ctx = {"form" : form}
    return render(req,"posts/create.html",ctx)

  form = PostForm(req.POST,req.FILES)
  if form.is_valid():
    form.save()
  return redirect("posts:main")


def detail(req, pk):
  post = Post.objects.get(id=pk)
  user = post.user
  related_posts = user.post_set.all()
  ctx = {'post':post}
  return render(req,'posts/detail.html',ctx)


def delete(req,pk):
  if req.method == "POST":
    Post.objects.get(id=pk).delete()
  return redirect("posts:main")

def update(req,pk):
  post = Post.objects.get(id=pk)
  
  if req.method == "GET":
    form = PostForm(instance=post)
    ctx = {'form':form,'pk':pk}
    return render(req,'posts/update.html',ctx)
  
  form = PostForm(req.POST,req.FILES,instance=post)
  if form.is_valid():
    form.save()
  return redirect("posts:detail",pk)