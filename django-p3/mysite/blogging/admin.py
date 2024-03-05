from django.contrib import admin
from blogging.models import Post, Category, CategoryAdmin, PostAdmin
# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)