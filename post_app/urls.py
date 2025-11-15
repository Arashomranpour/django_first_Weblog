from django.urls import path
from . import views


app_name="post"
urlpatterns = [
    path("detail/<slug:slug>",views.post_detail,name="article_detail"),
    path("list", views.all_posts.as_view(), name="all_posts"),
    path("category/<int:pk>",views.category_detail.as_view(),name="category_detail"),
    path("search/",views.search,name="search"),
    path("contactus/",views.ContactusView.as_view(),name="contactus"),
    path("allmessages/",views.MessageListView.as_view(),name="allmessages"),
    # path("allmessages/edit/<int:pk>",views.MessageUpdate.as_view(),name="messageedit"),
    path("allmessages/delete/<int:pk>",views.MessageDelete.as_view(),name="MessageDelete"),
    path("like/<slug:slug>/<int:pk>",views.Likeview,name="like"),

]
