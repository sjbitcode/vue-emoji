from django.test import TestCase

from emojis.models import Emoji, SubCategory, MainCategory, Keyword


class TestEmojiModel(TestCase):
	def setUp(self):
		self.emoji_pizza = Emoji.objects.create(
			shortcode='pizza',
			codepoint='\\U0001F355'
		)

	def test_shortened_codepoint(self):
		self.assertEqual(self.emoji_pizza.shortened_codepoint, 'U+1F355')

	def test_surrogate_pairs(self):
		self.assertEqual(self.emoji_pizza.surrogate_pairs, '"\\ud83c\\udf55"')


class TestCategory(TestCase):
	def setUp(self):
		self.main_category_food = MainCategory.objects.create(name='Food & Drink')
		self.sub_category_food = SubCategory.objects.create(name='food-prepared', parent_category=self.main_category_food)
		self.sub_category_fruit = SubCategory.objects.create(name='food-fruit', parent_category=self.main_category_food)

	def test_main_category(self):
		self.assertEqual(len(self.main_category_food.sub_categories.all()), 2)

	def test_sub_categories(self):
		self.assertEqual(self.sub_category_food.parent_category, self.main_category_food)
		self.assertEqual(self.sub_category_fruit.parent_category, self.main_category_food)


class TestKeyword(TestCase):
	def setUp(self):
		self.emoji_pizza = Emoji.objects.create(
			shortcode='pizza',
			codepoint='\\U0001F355'
		)
		self.emoji_cheese = Emoji.objects.create(
			shortcode='cheese_wedge',
			codepoint='\\U0001F9C0'
		)

		self.keyword_cheese = Keyword.objects.create(name='cheese')
		self.keyword_pizza = Keyword.objects.create(name='pizza')
		self.keyword_cheese_wedge = Keyword.objects.create(name='cheese wedge')

		self.emoji_pizza.keywords.add(self.keyword_cheese, self.keyword_pizza)
		self.emoji_pizza.save()

		self.emoji_cheese.keywords.add(self.keyword_cheese, self.keyword_cheese_wedge)
		self.emoji_cheese.save()

	def test_keyword_in_emoji(self):
		self.assertIn(self.emoji_pizza, self.keyword_cheese.emojis.all())
		self.assertIn(self.emoji_cheese, self.keyword_cheese.emojis.all())
