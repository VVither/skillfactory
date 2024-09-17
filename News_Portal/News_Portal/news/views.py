from django.shortcuts import render, get_object_or_404
from .models import Post
from datetime import datetime

def news_list(request):
    posts = Post.objects.all().order_by('-created_at')  # Сортировка от новых к старым
    return render(request, 'news/news_list.html', {
        'posts': posts,
        'post_count': posts.count(), # Колличество новостей
        'year': datetime.now().year # Текущий год
    })

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)  # Получаем пост по id или 404 если не найден пост
    return render(request, 'news/post_detail.html', {'post' : post}) # Передаём пост в шаблон