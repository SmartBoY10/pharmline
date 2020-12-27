from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from .forms import ContactForm
from .models import *

def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            mail = send_mail(
                form.cleaned_data['number'],  
                form.cleaned_data['content'], 
                'qurol.django99@gmail.com', 
                ['qurol.abdujalilov99@gmail.com'], 
                fail_silently=True)
            if mail:
                messages.success(request, 'Письмо отправлено!')
                return redirect('home')
            else:
                messages.error(request, 'Ошибка отправки')
        else:
            messages.error(request, 'Ошибка валидации')
    else:
        form = ContactForm()

    about = AboutUs.objects.all()
    catalogs = CatalogInfo.objects.all()
    consulting = Consulting.objects.all()
    return render(request, 'pharmshop/index.html', {'about': about, 'catalogs': catalogs, 'consulting': consulting, "form": form})




def about(request):
    about_ = AboutUs.objects.all()
    categories = Category.objects.all()
    return render(request, 'pharmshop/about.html', {'about_': about_, 'categories': categories})



def properties(request):
    medicines = Product.objects.filter(category=2)
    medical_devices = Product.objects.filter(category=1)
    return render(request, 'pharmshop/properties.html', {'medicines': medicines, 'medical_devices': medical_devices})



class ProductDetailView(View):
    def get(self, request, slug):
        product = Product.objects.get(slug=slug)
        return render(request, 'pharmshop/product_detail.html', {'product': product})



def services(request):
    return render(request, 'pharmshop/services.html')


def articles(request):
    articles = Article.objects.all()
    return render(request, 'pharmshop/articles.html', {'articles': articles})


class ArticleDetailView(View):
    def get(self, request, slug):
        article = Article.objects.get(slug=slug)
        return render(request, 'pharmshop/article_detail.html', {'article': article})


def videos(request):
    videos = Video.objects.all()
    return render(request, 'pharmshop/videos.html', {'videos': videos})


class VideoDetailView(View):
    def get(self, request, slug):
        video = Video.objects.get(slug=slug)
        videofile= video.video.url
        return render(request, 'pharmshop/video_detail.html', {'video_url': videofile, 'video': video})