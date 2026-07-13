from django.contrib import admin

from .models import Category, Post, Comment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created_at']
    prepopulated_fields = {'slug': ('name',)}  # auto-fill slug from name
    search_fields = ['name']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'status', 'published_at']
    list_filter = ['status', 'category', 'created_at']
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ['author']
    date_hierarchy = 'published_at'
    ordering = ['-published_at']

    # These fields appear grouped in the detail view:
    fieldsets = (
        ('Post Information', {
            'fields': ('title', 'slug', 'author', 'category', 'status')
        }),
        ('Content', {
            'fields': ('content', 'excerpt', 'cover_image')
        }),
        ('Dates', {
            'fields': ('published_at',),
            'classes': ('collapse',)  # hidden by default
        }),
    )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'post', 'created_at', 'is_active']
    list_filter = ['is_active', 'created_at']
    search_fields = ['body', 'author__username']
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(is_active=True)
        self.message_user(request, f'{queryset.count()} comment(s) approved.')
    approve_comments.short_description = 'Approve selected comments'