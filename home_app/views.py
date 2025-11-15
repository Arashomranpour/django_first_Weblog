from django.shortcuts import render,redirect
from post_app.models import Article,Category
from django.urls import reverse
from django.shortcuts import get_object_or_404
# Create your views here.
def home(request):
    articles = Article.objects.all()
    # print(reverse("post:article_detail",args=[3])
    category=Category.objects.all()
    # category=get_object_or_404(Category)
    # print(category)
    return render(request, "home_app/index.html",{"articles": articles , "category":category})



def sidebar(request):
    context={}
    return render(request,"includes/sidebar.html",context)