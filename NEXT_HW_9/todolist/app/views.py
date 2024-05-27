from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Post
from django.utils import timezone
from django.utils.timezone import now, localtime


# Create your views here.

def home(request):
    posts = Post.objects.all()
    for post in posts:
        if post.due_date:
            delta = post.due_date - localtime(now())
            # due_date가 오늘인 경우
            if delta.days == 0 and delta.seconds > 0:
                post.d_day_text = "D-Day"
            elif delta.days < 0:
                post.d_day_text = "기한 만료"
            else:
                post.d_day_text = f"D-{delta.days}"
        else:
            post.d_day_text = "기한 없음"
    return render(request, 'home.html', {'posts': posts})

def new(request):
    if request.method == "POST":
        # POST 요청을 처리하는 코드가 여기 들어가며, 모든 줄은 함수 정의에 대해 들여쓰기가 되어야 합니다.
        title = request.POST.get('title')
        content = request.POST.get('content')
        due_date = request.POST.get('due_date')
        
        if due_date == '':
            due_date = None
        
        post = Post(title=title, content=content, due_date=due_date)
        post.save()
        
        return redirect('home')  # 'home'은 여러분의 홈페이지를 가리키는 URL 패턴의 이름입니다.
    else:
        # GET 요청을 처리하는 코드가 여기 들어가며, 이 줄도 들여쓰기가 되어야 합니다.
        return render(request, 'new.html')
    
def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        if "delete" in request.POST:  # 삭제 버튼을 클릭한 경우
            post.delete()
            return HttpResponseRedirect(reverse('home'))
        else:  # 수정 폼을 제출한 경우
            post.title = request.POST.get('title')
            post.content = request.POST.get('content')
            post.due_date = request.POST.get('due_date')
            post.save()
            return redirect('home')
    return render(request, 'detail.html', {'post': post})