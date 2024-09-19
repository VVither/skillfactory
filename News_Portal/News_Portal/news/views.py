from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Post
from django.utils import timezone
from django.http import Http404
from .filters import PostFilter

class NewsListView(ListView):
    model = Post
    template_name = 'news/news_list.html' # Путь к шаблону
    context_object_name = 'posts' # Имя переменной которая будет использоваться в шаблоне 
    ordering = ['-created_at'] # Сортировка от новых к старым
    paginate_by = 10 # Укажите кол-во постов на 1 странице

    #def get_queryset(self): # Фильтр только новости
    #    return Post.objects.filter(post_type ='Новость')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_count'] = self.get_queryset().count # Кол-во постов
        context['year'] = timezone.now().year # Текущий год
        return context

class NewsDetailView(DetailView):
    model = Post
    template_name = 'news/post_detail.html'
    context_object_name = 'post'

    def get_object(self):
        post = get_object_or_404(Post, id=self.kwargs['post_id'])
    #    if post.post_type != 'Новость':
    #       raise Http404('Новость не найдена.')
        return post
    
class SearchResultsView(ListView):
    model = Post
    template_name = 'news/search_result.html'
    context_object_name = 'post'
    
    def get_queryset(self):
        queryset = Post.objects.all()
        self.filterset = PostFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs  # Возвращаем отфильтрованный queryset