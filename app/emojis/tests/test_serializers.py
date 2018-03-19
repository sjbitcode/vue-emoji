from django.test import TestCase

from emojis.models import Emoji, MainCategory, SubCategory, Keyword
from emojis.serializers import EmojiSerializer, SubCategorySerializer, MainCategorySerializer


class TestEmojiSerializer(TestCase):
	def setUp(self):

		self.main_category_food = MainCategory.objects.create(name='Food & Drink')
		self.main_category_animals = MainCategory.objects.create(name='Animals & Nature')
		self.main_category_smileys = MainCategory.objects.create(name='Smileys & People')

		self.sub_category_food = SubCategory.objects.create(name='food-prepared', parent_category=self.main_category_food)
		self.sub_category_mammal = SubCategory.objects.create(name='animal-mammal', parent_category=self.main_category_animals)
		self.sub_category_emoticon = SubCategory.objects.create(name='emoticon', parent_category=self.main_category_smileys)
		self.sub_category_fruit = SubCategory.objects.create(name='food-fruit', parent_category=self.main_category_food)

		self.keyword_cheesy = Keyword.objects.create(name='cheesy')
		self.keyword_pizza = Keyword.objects.create(name='pizza')

		self.emoji_pizza = Emoji.objects.create(
			shortcode='pizza',
			codepoint='\\U0001F355',
			main_category=self.main_category_food,
			sub_category=self.sub_category_food
		)
		self.emoji_pizza.keywords.add(self.keyword_cheesy, self.keyword_pizza)
		self.emoji_pizza.save()

		self.emoji_rabbit = Emoji.objects.create(
			shortcode='rabbit',
			codepoint='\\U0001F407',
			main_category=self.main_category_animals,
			sub_category=self.sub_category_mammal
		)

	def test_single_emoji_contains_expected_fields(self):
		data = EmojiSerializer(self.emoji_pizza).data
	
		self.assertEqual(
			set(data.keys()),
			set([
				'sub_category', 
				'shortened_codepoint',
				'codepoint',
				'surrogate_pairs',
				'keywords',
				'main_category',
				'shortcode'
			]))

	def test_single_emoji_keywords(self):
		data = EmojiSerializer(self.emoji_pizza).data
		self.assertEqual(set(data.get('keywords')), set(['cheesy', 'pizza']))

	def test_serialize_multiple_emoji(self):
		data = EmojiSerializer([self.emoji_pizza, self.emoji_rabbit], many=True).data
		self.assertEqual(len(data), 2)

	def test_single_sub_category_contains_expected_fields(self):
		data = SubCategorySerializer(self.sub_category_mammal).data
		self.assertEqual(list(data.keys()), ['name'])

	def test_serialize_multiple_sub_categories(self):
		sub_categories = [
			self.sub_category_food,
			self.sub_category_mammal,
			self.sub_category_emoticon
		]
		data = SubCategorySerializer(sub_categories, many=True).data
		self.assertEqual(len(data), 3)

	def test_single_main_category_contains_expected_fields(self):
		data = MainCategorySerializer(self.main_category_food).data
		self.assertEqual(set(data.keys()), set(['name', 'subcategories']))
		self.assertEqual(set(data.get('subcategories')), set(['food-prepared', 'food-fruit']))


	def test_serialize_multiple_main_categories(self):
		main_categories = [
			self.main_category_food,
			self.main_category_animals,
			self.main_category_smileys
		]
		data = MainCategorySerializer(main_categories, many=True).data
		self.assertEqual(len(data), 3)


