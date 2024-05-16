from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render, get_object_or_404
from django.http import JsonResponse, HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .models import Comment, Post, Like

def signup(request):
   if request.method == 'POST':
      username = request.POST['username']
      password = request.POST['password']
      exist_user = User.objects.filter(username=username)
      if exist_user:
           error = "이미 존재하는 유저입니다."
           return render(request, 'registration/signup.html', {"error":error})
      
      new_user = User.objects.create_user(username=username, password=password)
      auth.login(request, new_user)
   
      return redirect('home')
       
   return render(request, 'registration/signup.html')

def login(request):
   if request.method == 'POST':
      username = request.POST['username']
      password = request.POST['password']
      user = auth.authenticate(username=username, password=password)
      if user is not None:
           auth.login(request, user)
           return redirect(request.GET.get('next', '/'))
      error = "아이디 또는 비밀번호가 틀립니다"
      return render(request, 'registration/login.html', {"error":error})
        
   return render(request, 'registration/login.html')

def home(request):
   posts = Post.objects.all()
   return render(request, 'home.html', {'posts':posts})

def logout(request):
   auth.logout(request)
   return redirect('home')

@login_required(login_url="/registration/login/")
def new(request):
   if request.method == "POST":
       title = request.POST['title']
       content = request.POST['content']
       new_post = Post.objects.create(
           title=title,
           content=content,
           author=request.user
       )
       return redirect('detail', new_post.pk)
  
   return render(request, 'new.html')

@login_required(login_url="/registration/login/")
def detail(request, post_pk):
   post = get_object_or_404(Post, pk=post_pk)
   return render(request, 'detail.html', {'post': post})

@csrf_exempt
@login_required(login_url="/registration/login/")
def add_comment(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        post_pk = data.get('post_pk')
        content = data.get('content')
        post = get_object_or_404(Post, pk=post_pk)
        
        new_comment = Comment.objects.create(
            post=post,
            content=content,
            author=request.user
        )
        
        return JsonResponse({'id': new_comment.id, 'content': new_comment.content, 'author': new_comment.author.username})

@csrf_exempt
@login_required(login_url="/registration/login/")
def delete_comment(request, comment_pk):
    if request.method == 'POST':
        comment = get_object_or_404(Comment, pk=comment_pk)
        if comment.author == request.user:
            comment.delete()
            return JsonResponse({'status': 'deleted'})
        else:
            return JsonResponse({'status': 'unauthorized'}, status=403)

@csrf_exempt
@login_required(login_url="/registration/login/")
def edit_comment(request, comment_pk):
    if request.method == 'POST':
        data = json.loads(request.body)
        content = data.get('content')
        comment = get_object_or_404(Comment, pk=comment_pk)
        
        if comment.author == request.user:
            comment.content = content
            comment.save()
            return JsonResponse({'status': 'updated', 'content': comment.content})
        else:
            return JsonResponse({'status': 'unauthorized'}, status=403)

def edit(request, post_pk):
   post = get_object_or_404(Post, pk=post_pk)
   if request.method == 'POST':
       title = request.POST['title']
       content = request.POST['content']
       Post.objects.filter(pk=post_pk).update(
           title=title,
           content=content
       )
       return redirect('detail', post_pk)
   return render(request, 'edit.html', {'post':post})

def delete(request, post_pk):
   post = get_object_or_404(Post, pk=post_pk)
   post.delete()
   return redirect('home')

@csrf_exempt
def like(request):
   if request.method == 'POST':
      request_body = json.loads(request.body)
      post_pk = request_body['post_pk']
      post = get_object_or_404(Post, pk=post_pk)
      user_like = Like.objects.filter(user=request.user, post=post)
      if user_like.exists():
         user_like.delete()
      else:
         Like.objects.create(post=post, user=request.user)
      response = {'like_count': post.likes.count()}
      return HttpResponse(json.dumps(response))
