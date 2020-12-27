from modeltranslation.translator import register, TranslationOptions
from .models import *

@register(AboutUs)
class AboutUsTranslationOptions(TranslationOptions):
    fields = ('title', 'tagline', 'company_year', 'content')

@register(Consulting)
class ConsultingTranslationOptions(TranslationOptions):
    fields = ('title', 'tagline', 'content')

@register(CatalogInfo)
class CatalogInfoTranslationOptions(TranslationOptions):
    fields = ('title', 'tagline', 'content')


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'mode_of_application', 'active_substance', 'description', 'drug_action', 'structure', 'release_forms')

@register(Article)
class ArticleTranslationOptions(TranslationOptions):
    fields = ('title', 'tagline', 'content')

@register(Video)
class VideoTranslationOptions(TranslationOptions):
    fields = ('title', 'tagline', 'content')
