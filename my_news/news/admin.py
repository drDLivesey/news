from django.contrib import admin

# Register your models here.

from .models import Post
from .models import Tag


class PostModelAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "updated", "timestamp"]
    list_display_links = ["id", "updated"]
    list_editable = ["title"]
    list_filter = ["updated", "timestamp"]
    search_fields = ["title", "content"]

    class Meta:
        model = Post


class TagModelAdmin(admin.ModelAdmin):

    class Meta:
        model = Tag


admin.site.register(Post, PostModelAdmin)
admin.site.register(Tag, TagModelAdmin)