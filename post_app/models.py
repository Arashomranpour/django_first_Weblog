from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.html import format_html
from django.utils.text import slugify 
# Create your models here.




class Category(models.Model):
    name = models.CharField(max_length=255)
    created=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

    class Meta:
        ordering = ("-created",)


class Article(models.Model):
    author=models.ForeignKey(User, verbose_name="author name" , on_delete=models.CASCADE)
    title = models.CharField(unique=True,)
    category=models.ManyToManyField(Category, verbose_name="category / categories")
    body=models.TextField()
    image=models.ImageField(upload_to="images/articles",blank=True,null=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    status=models.BooleanField(default=True)
    slug=models.SlugField( unique=True,blank=True)


    class Meta:
        ordering = ("-updated",)
    

    def get_absolute_url(self):
        return reverse("post:article_detail",kwargs={"slug":self.slug})
    
    def __str__(self):
        return f"{self.id} :{self.title} - {self.body[:30]}"
    def save(self, *args, **kwargs):
        self.slug=slugify(self.title)
        return super().save(*args, **kwargs)

    def show_image(self):
        if self.image:
            return format_html(
                '<a href="{}" target="_blank">'
                '<img src="{}" width="50" height="50" style="object-fit:cover; border-radius:4px;" />'
                '</a>',
                self.image.url,  # link target
                self.image.url  # thumbnail source
            )
        return "No image"

    show_image.short_description = "Image"

class Comments(models.Model):
    user=models.ForeignKey(User, verbose_name="author name" , on_delete=models.CASCADE)
    article=models.ForeignKey(Article, verbose_name="article", on_delete=models.CASCADE,related_name="comments")
    body=models.TextField()
    parents= models.ForeignKey("self",on_delete=models.CASCADE,related_name="replies",blank=True,null=True )
    created=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.body[:20]
    class Meta:
        ordering = ("-created",)
        verbose_name="comments"
        verbose_name_plural="comments"


class messagecontactus(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created=models.DateTimeField(auto_now_add=True,null=True)
    read=models.BooleanField(default=False)
    def __str__(self):
        return self.subject

    class Meta:
        ordering = ("-created",)


class Like(models.Model):
    user=models.ForeignKey(User, verbose_name="author name" , on_delete=models.CASCADE)
    article=models.ForeignKey(Article, verbose_name="article", on_delete=models.CASCADE,related_name="like")
    created=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.user} :{self.article}"
    class Meta:
        verbose_name="like"
        verbose_name_plural="likes"
        ordering = ("-created",)
