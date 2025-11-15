from django.contrib import admin
from .models import Article,Category,Comments,messagecontactus,Like

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]


class CommentInline(admin.TabularInline):
    model = Comments



@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["id","author","title","show_image"]
    list_editable = ["title"]
    list_filter = ["status"]
    search_fields = ["title"]
    inlines = (CommentInline,)



admin.site.register(Comments)
admin.site.register(Like)
admin.site.register(messagecontactus)