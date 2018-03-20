import json

from django.db.models import Q
from django.test import TestCase
from django.urls import reverse
from django.utils.http import urlencode
from rest_framework import status
from rest_framework.test import APIClient

from emojis.models import Emoji, SubCategory, MainCategory, Keyword
from emojis.serializers import EmojiSerializer, MainCategorySerializer


# initialize the API Client
client = APIClient()

def reverse_querystring(view, urlconf=None, args=None, kwargs=None, current_app=None, query_kwargs=None):
    '''
    src: https://gist.github.com/benbacardi/227f924ec1d9bedd242b
    Custom reverse to handle query strings.
    Usage: reverse('app.views.my_view', kwargs={'pk': 123}, query_kwargs={'search', 'Bob'})
    '''
    base_url = reverse(view, urlconf=urlconf, args=args, kwargs=kwargs, current_app=current_app)
    if query_kwargs:
        return '{}?{}'.format(base_url, urlencode(query_kwargs))
    return base_url

class RootEndpoint(TestCase):
	def setUp(self):
		self.endpoint = 'hello'

	def test_root_endpoint(self):
		response = client.get(reverse(self.endpoint))

		self.assertEqual(response.status_code, status.HTTP_200_OK)


class EmojiEndpoint(TestCase):
	def setUp(self):

		# Emoji endpoint url
		self.endpoint = 'emoji'

		# Main Category objects
		self.main_category_food = MainCategory.objects.create(name='Food & Drink')
		self.main_category_smileys = MainCategory.objects.create(name='Smileys & People')
		self.main_category_objects = MainCategory.objects.create(name='Objects')

		# Sub Category objects
		self.sub_category_food_prepared = SubCategory.objects.create(
			name='food-prepared', parent_category=self.main_category_food
		)
		self.sub_category_fruit = SubCategory.objects.create(
			name='food-fruit', parent_category=self.main_category_food
		)
		self.sub_category_vegetable = SubCategory.objects.create(
			name='food-vegetable', parent_category=self.main_category_food
		)
		self.sub_category_book = SubCategory.objects.create(
			name='book-paper', parent_category=self.main_category_objects
		)
		self.sub_category_emotion = SubCategory.objects.create(
			name='emotion', parent_category=self.main_category_smileys
		)
		self.sub_category_face_positive = SubCategory.objects.create(
			name='face-positive', parent_category=self.main_category_smileys
		)

		# Emoji objects
		self.emoji_salad = Emoji.objects.create(
			shortcode='green_salad',
			codepoint='\\U0001F957',
			main_category=self.main_category_food,
			sub_category=self.sub_category_food_prepared
		)

		self.green_apple = Emoji.objects.create(
			shortcode='green_apple',
			codepoint='\\U0001F34F',
			main_category=self.main_category_food,
			sub_category=self.sub_category_fruit
		)

		self.mango = Emoji.objects.create(
			shortcode='⊛_mango',
			codepoint='\\U0001F96D',
			main_category=self.main_category_food,
			sub_category=self.sub_category_fruit
		)

		self.emoji_leafy_green = Emoji.objects.create(
			shortcode='⊛_leafy_green',
			codepoint='\\U0001F96C',
			main_category=self.main_category_food,
			sub_category=self.sub_category_vegetable
		)

		self.emoji_green_book = Emoji.objects.create(
			shortcode='green_book',
			codepoint='\\U0001F4D7',
			main_category=self.main_category_objects,
			sub_category=self.sub_category_book
		)

		self.emoji_blue_book = Emoji.objects.create(
			shortcode='blue_book',
			codepoint='\\U0001F4D8',
			main_category=self.main_category_objects,
			sub_category=self.sub_category_book
		)

		self.emoji_green_heart = Emoji.objects.create(
			shortcode='green_heart',
			codepoint='\\U0001F49A',
			main_category=self.main_category_smileys,
			sub_category=self.sub_category_emotion
		)


	def test_get_all_emoji(self):
		# API response
		response = client.get(reverse(self.endpoint))

		# Get data from db
		emoji = Emoji.objects.all()
		serializer = EmojiSerializer(emoji, many=True)

		self.assertEqual(len(response.data.get('results')), len(serializer.data))
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_get_emoji_by_main_category(self):
		# API response
		url = reverse_querystring(self.endpoint, query_kwargs={'main_category': self.main_category_food})
		response = client.get(url)

		# Get data from db
		emoji = Emoji.objects.filter(main_category__name__icontains=self.main_category_food)
		serializer = EmojiSerializer(emoji, many=True)

		self.assertEqual(len(response.data.get('results')), len(serializer.data))
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_get_emoji_by_sub_category(self):
		# API response
		url = reverse_querystring(self.endpoint, query_kwargs={'sub_category': self.sub_category_fruit})
		response = client.get(url)

		# Get data from db
		emoji = Emoji.objects.filter(sub_category__name__icontains=self.sub_category_fruit)
		serializer = EmojiSerializer(emoji, many=True)

		self.assertEqual(len(response.data.get('results')), len(serializer.data))
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_get_emoji_by_both_categories(self):
		# API response
		url = reverse_querystring(self.endpoint, query_kwargs={
			'main_category': self.main_category_food,
			'sub_category': self.sub_category_fruit
		})
		response = client.get(url)

		# Get data from db
		query = Q(
				Q(main_category__name__icontains=self.main_category_food)
				& Q(sub_category__name__icontains=self.sub_category_fruit)
			)
		emoji = Emoji.objects.filter(query)
		serializer = EmojiSerializer(emoji, many=True)

		self.assertEqual(len(response.data.get('results')), len(serializer.data))
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_get_flat_emoji(self):
		query_string = 'blue'

		# API response
		url = reverse_querystring(self.endpoint, query_kwargs={'q': query_string, 'flat': True})
		response = client.get(url)

		# API results list
		results = response.data.get('results')

		self.assertEqual(len(results), 1)
		self.assertEqual(
			set(results[0].keys()),
			set([
				'shortcode',
				'codepoint',
				'surrogate_pairs',
				'shortened_codepoint'
			]))

	def test_get_all_recent_emoji(self):
		# API response
		url = reverse_querystring(self.endpoint, query_kwargs={'recent': True})
		response = client.get(url)

		# Get data from db
		emoji = Emoji.objects.filter(shortcode__startswith='\u229b')
		serializer = EmojiSerializer(emoji, many=True)

		self.assertEqual(len(response.data.get('results')), len(serializer.data))
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_get_limited_emoji(self):
		limit = 3

		# API response
		url = reverse_querystring(self.endpoint, query_kwargs={'limit': limit})
		response = client.get(url)

		# Get data from db
		emoji = Emoji.objects.all()[:limit]
		serializer = EmojiSerializer(emoji, many=True)

		self.assertEqual(len(response.data.get('results')), len(serializer.data))
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_get_emoji_by_querystring(self):
		query_string = 'green'

		# API response
		url = reverse_querystring(self.endpoint, query_kwargs={'q': query_string})
		response = client.get(url)

		# Get data from db
		query_filter = Q(
				Q(shortcode__icontains=query_string) |
				Q(codepoint__icontains=query_string) |
				Q(keywords__name__icontains=query_string)
			)
		emoji = Emoji.objects.filter(query_filter)
		serializer = EmojiSerializer(emoji, many=True)

		self.assertEqual(len(response.data.get('results')), len(serializer.data))
		self.assertEqual(response.status_code, status.HTTP_200_OK)


class CategoriesEndpoint(TestCase):
	def setUp(self):
		# Category endpoint url
		self.endpoint = 'categories'

		# Main Category objects
		self.main_category_food = MainCategory.objects.create(name='Food & Drink')
		self.main_category_smileys = MainCategory.objects.create(name='Smileys & People')
		self.main_category_objects = MainCategory.objects.create(name='Objects')

		# Sub Category objects
		self.sub_category_food_prepared = SubCategory.objects.create(
			name='food-prepared', parent_category=self.main_category_food
		)
		self.sub_category_fruit = SubCategory.objects.create(
			name='food-fruit', parent_category=self.main_category_food
		)
		self.sub_category_vegetable = SubCategory.objects.create(
			name='food-vegetable', parent_category=self.main_category_food
		)
		self.sub_category_book = SubCategory.objects.create(
			name='book-paper', parent_category=self.main_category_objects
		)
		self.sub_category_emotion = SubCategory.objects.create(
			name='emotion', parent_category=self.main_category_smileys
		)
		self.sub_category_face_positive = SubCategory.objects.create(
			name='face-positive', parent_category=self.main_category_smileys
		)

	def test_get_categories(self):
		# API response
		response = client.get(reverse(self.endpoint))

		# Get data from db
		main_categories = MainCategory.objects.all().order_by('id')
		serializer = MainCategorySerializer(main_categories, many=True)

		self.assertEqual(len(response.data.get('results')), len(serializer.data))
		self.assertEqual(response.status_code, status.HTTP_200_OK)


class StatsEndpoint(TestCase):
	def setUp(self):
		self.endpoint = 'stats'

	def test_get_stats(self):
		# API response
		response = client.get(reverse(self.endpoint))

		self.assertEqual(
			set(response.data.keys()),
			set([
				'date_requested',
				'Total Emojis',
				'Recently Added Emojis',
				'Total Main Categories',
				'Total Sub Categories',
				'Total Keywords'
			]))





