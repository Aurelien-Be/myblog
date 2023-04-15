from modeltranslation.translator import translator, register, TranslationOptions
from .models import Tag, Post

class TagTranslationOptions(TranslationOptions):
   fields = 'caption'

class PostTranslationOptions(TranslationOptions):
    fields=("title", 'excerpt','slug', 'content', 'tags')
     empty_values = {'slug': None}


translator.register(Post, PostTranslationOptions)
translator.register(Tag, TagTranslationOptions)

