from django.urls import path

from . import views

urlpatterns = [
	path(
		'api/v1', 
		views.HelloView.as_view(), 
		name='hello'
	),

	path(
		'api/v1/emoji',
		views.ListEmojis.as_view(),
		name='emoji'
	),

	path(
		'api/v1/homepage',
		views.ListSelectedEmojis.as_view(),
		name='homepage_select'
	),

	path(
		'api/v1/categories',
		views.ListCategories.as_view(),
		name='categories'
	),

	path(
		'api/v1/stats',
		views.Stats.as_view(),
		name='stats'
	)
]