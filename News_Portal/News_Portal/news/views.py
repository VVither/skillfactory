from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post
from django.utils import timezone
from .filters import PostFilter
from django.shortcuts import render
from .forms import PostForm

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
    
    # представление для поиска
def search_posts(request):
    f = PostFilter(request.GET, queryset=Post.objects.all())
    return render(request, 'news/search_result.html', {'filter': f})

class PostCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'news/post_edit.html'

class UpdateView(UpdateView):
    pass