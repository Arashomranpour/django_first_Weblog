from datetime import date

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy, reverse
from django.views.generic import View, FormView, ListView, UpdateView, DeleteView, CreateView

from .forms import Contactusform
from django.shortcuts import render, get_object_or_404, redirect
from .models import Article,Category,Comments,messagecontactus,Like
from django.core.paginator import Paginator
# Create your views here.
def post_detail(request,slug):
    article = get_object_or_404(Article, slug=slug)

    if request.method == 'POST':
        body = request.POST.get('body')
        parentid = request.POST.get('parentid')

        parent_comment = None
        if parentid:  # if replying to a comment
            try:
                parent_comment = Comments.objects.get(id=int(parentid))
            except Comments.DoesNotExist:
                parent_comment = None

        # Create comment (either parent or reply)
        Comments.objects.create(
            body=body,
            article=article,
            user=request.user,
            parents=parent_comment
        )

    latest=Article.objects.all()[:2]

    category=Category.objects.all()
    return render(request,"post_app/post-details.html", {"article":article,"latest":latest,"category":category})

#
# def all_posts(request):
#     all_posts=Article.objects.all()
#     page_number = request.GET.get('page')
#     paginator=Paginator(all_posts,2)
#     object_list=paginator.get_page(page_number)
#     return render(request, "post_app/post_list.html", {"article":object_list})
class all_posts(ListView):
    model = Article
    template_name = "post_app/post_list.html"
    context_object_name = 'article'
    paginate_by = 3
    queryset = Article.objects.filter(status=True)


# def category_detail(request,pk=None):
#     category=get_object_or_404(Category,id=pk)
#     category=category.article_set.all()
#     return render(request,"post_app/post_list.html", {"article":category})
class category_detail(ListView):
    model = Category
    template_name = "post_app/post_list.html"
    context_object_name = "article"

    def get_object(self):
        pk = self.kwargs.get('pk')  # ← this is where you get your argument
        return get_object_or_404(Category, id=pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["article"] = self.get_object().article_set.all()
        return context

def search(request):
    q=request.GET.get('q')
    articles=Article.objects.filter(title__icontains=q)
    page_number = request.GET.get('page')
    paginator = Paginator(articles, 3)
    object_list = paginator.get_page(page_number)
    return render(request,"post_app/post_list.html", {"article":object_list})


# def contactus(request):
#     # if request.user.is_authenticated:
#         if request.method=="POST":
#             form = Contactusform(data=request.POST)
#             if form.is_valid():
#                 form.save( )
#                 return redirect("home_app:home")
#
#
#         else:
#             form=Contactusform()
#         return render(request, "post_app/contactus.html",{"form":form})

class ContactusView(LoginRequiredMixin,CreateView):
    template_name = "post_app/contactus.html"
    form_class = Contactusform
    success_url = "/"
    login_url = "/login"
    # fields = ("subject", "message")
    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.email = self.request.user.email
        instance.save()
        return  super().form_valid(form)
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["message"]=messagecontactus.objects.all()
        return context


class MessageListView(ListView):
    model = messagecontactus
    template_name = "post_app/message_list.html"
    context_object_name = "message_list"
    def get_queryset(self):
        user=self.request.user
        if user.is_authenticated:
            return messagecontactus.objects.filter(email=user.email)
        else :
            return messagecontactus.objects.none()



# class MessageUpdate(UpdateView):
#     model = messagecontactus
#     template_name = "post_app/contactus.html"
#     fields = "__all__"
#     success_url = reverse_lazy("home_app:home")

class MessageDelete(DeleteView,LoginRequiredMixin):
    model=messagecontactus
    login_url = "/login"

    success_url = reverse_lazy("post:allmessages")
    template_name = "post_app/deletemessage.html"

@login_required(login_url="/login")
def Likeview(request,slug,pk):
    try:
        like=Like.objects.get(article__slug=slug,user_id=request.user.id)
        like.delete()

    except:
        Like.objects.create(article_id=pk,user_id=request.user.id)

    return redirect("post:article_detail",slug=slug)

