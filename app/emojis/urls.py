from django.urls import re_path

from . import views

urlpatterns = [
	re_path(
		r'^v1/?$',
		views.HelloView.as_view(), 
		name='hello'
	),

	re_path(
		r'^v1/emoji/?$',
		views.ListEmojis.as_view(),
		name='emoji'
	),

	re_path(
		r'^v1/homepage/?$',
		views.ListSelectedEmojis.as_view(),
		name='homepage_select'
	),

	re_path(
		r'^v1/categories/?$',
		views.ListCategories.as_view(),
		name='categories'
	),

	re_path(
		r'^v1/stats/?$',
		views.Stats.as_view(),
		name='stats'
	)
]