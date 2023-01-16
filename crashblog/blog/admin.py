from django.contrib import admin

from .models import Post, Category, Comment,Reply

class CommentItemInline(admin.TabularInline):
    model = Comment
    raw_id_fields = ['post']

class ReplyItemInline(admin.TabularInline):
    model = Reply
    raw_id_fields = ['comment']

class PostAdmin(admin.ModelAdmin):
    search_fields = ['title', 'intro', 'body']
    list_display = ['title', 'slug', 'category', 'created_at', 'status']
    list_filter = ['category', 'created_at', 'status']
    inlines = [CommentItemInline]
    prepopulated_fields = {'slug': ('title',)}

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title']
    prepopulated_fields = {'slug': ('title',)}

class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'post', 'created_at']
    inlines = [ReplyItemInline]

class ReplayAdmin(admin.ModelAdmin):
    list_display = ['name', 'comment', 'created_at']


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Reply,ReplayAdmin)