from django.contrib import admin
from blog.models import Post, Category
 
class PostAdmin(admin.ModelAdmin):
    # fields display on change list
    list_display = ['title', 'description', 'created', 'published', 'category']
    # fields to filter the change list with
    list_filter = ['published', 'created']
    # fields to search in change list
    search_fields = ['title', 'description', 'content']
    # enable the date drill down on change list
    date_hierarchy = 'created'
    # enable the save buttons on top on change form
    save_on_top = True
	
    # prepopulate the slug from the title - big timesaver!
    prepopulated_fields = {"slug": ("title",)}
 
class CatAdmin(admin.ModelAdmin):
	list_display = ['name', 'description']
	search_fields = ['name', 'description']
	
	save_on_top = True
	
admin.site.register(Category, CatAdmin)
admin.site.register(Post, PostAdmin)
