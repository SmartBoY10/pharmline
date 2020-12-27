from django.db import models
from django.urls import reverse

class AboutUs(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    tagline = models.CharField(max_length=150, verbose_name='Слоган')
    company_year = models.CharField(max_length=100, verbose_name='История нашего бизнеса ...')
    content = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'О компании'
        verbose_name_plural = 'О компании'


class Consulting(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    tagline = models.CharField(max_length=100, verbose_name='Слоган')
    content = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Консультация'
        verbose_name_plural = 'Консультации'



class CatalogInfo(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    tagline = models.CharField(max_length=100, verbose_name='Слоган')
    content = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Каталог'
        verbose_name_plural = 'Каталоги'


class Category(models.Model):
    name = models.CharField("Категория", max_length=150)
    slug = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Названия')
    description = models.TextField(verbose_name='Описания')
    photo = models.ImageField(verbose_name="Фото", upload_to="products/")
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True)
    price = models.IntegerField(default=0, verbose_name='Цена(сум)')
    mode_of_application = models.CharField(max_length=500, verbose_name='Способ применение', null=True)
    active_substance = models.CharField(max_length=500, verbose_name='Действующее вещество', null=True)
    drug_action = models.CharField(max_length=500, verbose_name='Действие препарата', null=True)
    structure = models.TextField(verbose_name='Состав', null=True)
    release_forms = models.CharField(max_length=500, verbose_name='Формы выпуска', null=True)
    slug = models.SlugField(max_length=130, unique=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"



class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовка')
    photo = models.ImageField(verbose_name="Фото", upload_to="articles/", null=True)
    tagline = models.CharField(max_length=200, verbose_name='Слоган', null=True)
    content = models.TextField(verbose_name='Текст')
    slug = models.SlugField(max_length=200, unique=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"


class Video(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовка')
    video = models.FileField(verbose_name="Видео", upload_to="videos/", null=True)
    tagline = models.CharField(max_length=200, verbose_name='Слоган', null=True)
    content = models.TextField(verbose_name='Текст')
    slug = models.SlugField(max_length=200, unique=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("video_detail", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = "Видео ролик"
        verbose_name_plural = "Видео ролики"
