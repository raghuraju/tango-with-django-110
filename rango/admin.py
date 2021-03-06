from django.contrib import admin
from .models import Category, Page, UserProfile

class PageInline(admin.TabularInline):
	model = Page
	extra = 3

class CategoryAdmin(admin.ModelAdmin):
	fieldsets = [
		('Name', {'fields': ['name']}),
		('Views & Likes', {'fields': ['views','likes'], 'classes': ('extrapretty',)})
	]
	inlines = [PageInline]
	list_display = ('name','views','likes')
	search_fields = ['name']

	# prepopulated_fields = {'slug':('name',)}

class PageAdmin(admin.ModelAdmin):
	# fields = ['title','category','url']
	fieldsets = [
		(None, {'fields': ['category']}),
		('Page Details', {'fields': ['title','url','views']}),
	]
	list_display = ('title','category','url')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)