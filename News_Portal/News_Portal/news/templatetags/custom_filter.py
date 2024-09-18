from django import template
from News_Portal import settings

register = template.Library()

@register.filter(name='censor')
def censor(value):
      """ Заменяет буквы в нежелательных слов в строке на '*' """
      # Получаем список нежелательных слов из настроек
      bad_words_list = [word.strip().lower() for word in settings.BAD_WORDS.split(',')]
      
      for word in bad_words_list:
         value = value.replace(word, '*' * len(word))
      
      return value