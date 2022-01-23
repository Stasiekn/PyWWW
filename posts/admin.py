from django.contrib import admin
from import_export import resources
from import_export.admin import ExportMixin

from .models import Post


class PostResource(resources.ModelResource):
    class Meta:
        model = Post


@admin.register(Post)
class PostAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ["id", "title", "created", "modified", "published", "spondored" ]
    search_fields = ["title", "description"]
    list_filter = ["published", "spondored"]
    resource_class = PostResource
#admin.site.register(Post)
