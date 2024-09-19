from django.urls import path
from .views import NewsListView, NewsDetailView, SearchResultsView

urlpatterns = [
    path('', NewsListView.as_view(), name='news_list'), # Общий список новостей
    path('<int:post_id>/', NewsDetailView.as_view(), name='post_detail'), # Подробности поста
    path('search/', SearchResultsView.as_view(), name='search_result')
]