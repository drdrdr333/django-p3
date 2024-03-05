from typing import Any
from django.contrib import admin
from django.db import models
from django.contrib.auth.models import User
from django.forms.models import ModelMultipleChoiceField
from django.http.request import HttpRequest


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    posts = models.ManyToManyField(Post, blank=True, through='PostCategory')

    class Meta:
        verbose_name_plural = "Catgories"

    def __str__(self):
        return self.name

class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class PostCategoryInLine(admin.TabularInline):
    model = Category.posts.through

class PostAdmin(admin.ModelAdmin):
    inlines = [
        PostCategoryInLine,
    ]

class CategoryAdmin(admin.ModelAdmin):
    pass