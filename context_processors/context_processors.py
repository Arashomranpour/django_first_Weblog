from post_app.models import Article,Category

def recent_posts(request):
    recent_posts = Article.objects.all().order_by('-created')[:3]
    return {"recent_posts": recent_posts}
def category_list(request):
    category_list = Category.objects.all()
    # print(category_list)
    return {"category_list": category_list}
