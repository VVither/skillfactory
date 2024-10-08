from django.urls import path
from .views import NewsListView, NewsDetailView, search_posts, PostCreate

app_name = 'news'

urlpatterns = [
    path('', NewsListView.as_view(), name='news_list'), # Общий список новостей
    path('<int:post_id>/', NewsDetailView.as_view(), name='post_detail'), # Подробности поста
    path('search/', search_posts, name='search'), # Поиск
    path('create/', PostCreate.as_view(), name='post_create') # Создание постов
]
