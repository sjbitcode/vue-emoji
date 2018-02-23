from django.contrib import admin

from .models import Emoji, MainCategory, SubCategory, Keyword, UnicodeVersion 


class RecentlyAddedFilter(admin.SimpleListFilter):
	'''
	Custom filter to display recently added emojis
	from Unicode Consortium.
	'''
	title = 'Recently Added'
	parameter_name = 'recently_added'

	def lookups(self, request, model_admin):
		return (
			('recent', 'recent'),
		)

	def queryset(self, request, queryset):
		if self.value() == 'recent':
			return queryset.filter(shortcode__startswith='\u229b')


class EmojiAdmin(admin.ModelAdmin):
	list_display = ('shortcode', 'main_category', 'sub_category')
	readonly_fields = ('codepoint', 'shortcode', 'main_category', 'sub_category', 'keywords')
	list_filter = (RecentlyAddedFilter, 'main_category', 'sub_category')
	search_fields = ['shortcode', 'codepoint', 'sub_category', 'main_category']


admin.site.register(Emoji, EmojiAdmin)
admin.site.register(MainCategory)
admin.site.register(SubCategory)
admin.site.register(Keyword)
admin.site.register(UnicodeVersion)