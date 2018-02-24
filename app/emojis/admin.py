from django.contrib import admin
from django.db.models import Q

from .models import Emoji, MainCategory, SubCategory, Keyword, UnicodeVersion 


class InputFilter(admin.SimpleListFilter):
	# https://medium.com/@hakibenita/how-to-add-a-text-filter-to-django-admin-5d1db93772d8
    template = 'admin/input_filter.html'

    def lookups(self, request, model_admin):
        # Dummy, required to show the filter.
        return ((),)

    def choices(self, changelist):
        # Grab only the "all" option.
        all_choice = next(super().choices(changelist))
        all_choice['query_parts'] = (
            (k, v)
            for k, v in changelist.get_filters_params().items()
            if k != self.parameter_name
        )
        yield all_choice


class KeywordFilter(InputFilter):
	parameter_name = 'keyword'
	title = 'keyword'

	def queryset(self, request, queryset):
		if self.value() is not None:
			keyword_list = self.value().split(',')

			return queryset.filter(keywords__name__in=keyword_list)


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
	list_filter = (RecentlyAddedFilter, KeywordFilter, 'main_category', 'sub_category',)
	search_fields = ['shortcode', 'codepoint']
	filter_horizontal = ('keywords',)


admin.site.register(Emoji, EmojiAdmin)
admin.site.register(MainCategory)
admin.site.register(SubCategory)
admin.site.register(Keyword)
admin.site.register(UnicodeVersion)
