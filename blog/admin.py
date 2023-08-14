from django.contrib import admin
from .models import(
    BlogCategory,
    Article,
)
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
	list_display = ('title','slug')
	search_fields = ('title', 'slug')
	prepopulated_fields = {'slug': ('title',)}


class ArticleAdmin(admin.ModelAdmin):
	list_display = ('title','slug', 'author','status')
	list_filter = ('publish','status', 'author')
	search_fields = ('title',)
	prepopulated_fields = {'slug': ('title',)}
	ordering = ['-status', '-publish']


admin.site.register(Article, ArticleAdmin)
admin.site.register(BlogCategory, CategoryAdmin)
