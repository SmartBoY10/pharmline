from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from modeltranslation.admin import TranslationAdmin

from .models import *

class AboutUsAdminForm(forms.ModelForm):
    content_ru = forms.CharField(widget=CKEditorUploadingWidget())
    content_en = forms.CharField(widget=CKEditorUploadingWidget())
    content_uz = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = AboutUs
        fields = '__all__'


class ConsultingAdminForm(forms.ModelForm):
    content_ru = forms.CharField(widget=CKEditorUploadingWidget())
    content_en = forms.CharField(widget=CKEditorUploadingWidget())
    content_uz = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Consulting
        fields = '__all__'


class CatalogInfoAdminForm(forms.ModelForm):
    content_ru = forms.CharField(widget=CKEditorUploadingWidget())
    content_en = forms.CharField(widget=CKEditorUploadingWidget())
    content_uz = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = CatalogInfo
        fields = '__all__'


class ProductAdminForm(forms.ModelForm):
    description_ru = forms.CharField(widget=CKEditorUploadingWidget())
    description_en = forms.CharField(widget=CKEditorUploadingWidget())
    description_uz = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Product
        fields = '__all__'


class ArticleAdminForm(forms.ModelForm):
    content_ru = forms.CharField(widget=CKEditorUploadingWidget())
    content_en = forms.CharField(widget=CKEditorUploadingWidget())
    content_uz = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Article
        fields = '__all__'


class VideoAdminForm(forms.ModelForm):
    content_ru = forms.CharField(widget=CKEditorUploadingWidget())
    content_en = forms.CharField(widget=CKEditorUploadingWidget())
    content_uz = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Video
        fields = '__all__'


class AboutUsAdmin(TranslationAdmin):
    form = AboutUsAdminForm
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    fields = ('title', 'tagline', 'company_year', 'content')
    search_fields = ('title',)
    save_on_top = True


class ConsultingAdmin(TranslationAdmin):
    form = ConsultingAdminForm
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    fields = ('title', 'tagline', 'content')
    search_fields = ('title',)
    save_on_top = True


class CatalogInfoAdmin(TranslationAdmin):
    form = CatalogInfoAdminForm
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    fields = ('title', 'tagline', 'content')
    search_fields = ('title',)
    save_on_top = True


class CategoryAdmin(TranslationAdmin):
    prepopulated_fields = {"slug": ('name',)}
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    save_on_top = True


class ProductAdmin(TranslationAdmin):
    form = ProductAdminForm
    prepopulated_fields = {"slug": ('name',)}
    list_display = ('id', 'name', 'category')
    list_display_links = ('id', 'name')
    list_filter = ('category',)
    search_fields = ('name',)
    fields = ('name', 'slug', 'photo', 'category', 'mode_of_application', 'active_substance', 'description', 'price', 'drug_action', 'structure', 'release_forms')
    save_on_top = True


class ArticleAdmin(TranslationAdmin):
    form = ArticleAdminForm
    prepopulated_fields = {"slug": ('title',)}
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    fields = ('title', 'slug', 'photo', 'tagline', 'content')
    search_fields = ('title',)
    save_on_top = True


class VideoAdmin(TranslationAdmin):
    form = VideoAdminForm
    prepopulated_fields = {"slug": ('title',)}
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    fields = ('title', 'slug', 'video', 'tagline', 'content')
    search_fields = ('title',)
    save_on_top = True


admin.site.register(AboutUs, AboutUsAdmin)
admin.site.register(Consulting, ConsultingAdmin)
admin.site.register(CatalogInfo, CatalogInfoAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Video, VideoAdmin)

admin.site.site_title = 'Управления компании'
admin.site.site_header = 'Управления компании'
