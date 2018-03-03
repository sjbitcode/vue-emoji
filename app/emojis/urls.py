from django.urls import path

from . import views

urlpatterns = [
	path(
		'', 
		views.HelloView.as_view(), 
		name='hello'
	),

	path(
		'emoji',
		views.ListEmojis.as_view(),
		name='emoji'
	),

	path(
		'categories',
		views.ListCategories.as_view(),
		name='categories'
	),

	path(
		'stats',
		views.Stats.as_view(),
		name='stats'
	)
]