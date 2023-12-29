from django.contrib import admin

from apps.posts.models import Post,Product

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created')
    search_fields = ('title', 'description')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')

# admin.site.register(Post)