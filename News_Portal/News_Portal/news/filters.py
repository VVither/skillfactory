import django_filters
from .models import Post
from django import forms

class PostFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains', label='Название')
    author = django_filters.CharFilter(field_name='author__name', lookup_expr='icontains', label='Имя автора')  # Предполагается, что у вас есть связь с автором
    date_after = django_filters.DateFilter(field_name='created_at', lookup_expr='gte', widget=forms.DateInput(attrs={'type': 'date'}), label='Позже даты')

    class Meta:
        model = Post
        fields = ['title', 'author', 'date_after']