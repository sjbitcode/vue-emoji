from rest_framework import serializers

from .models import Emoji, SubCategory, MainCategory


class EmojiSerializer(serializers.ModelSerializer):
	def __init__(self, *args, **kwargs):
		'''
		If query parameter, flat, is set to True, then return
		only shortcode and codepoints.
		'''
		super(EmojiSerializer, self).__init__(*args, **kwargs)

		flat = self.context['request'].query_params.get('flat')
		if flat in ['True', 'true', 'TRUE']:
			self.fields.pop('main_category')
			self.fields.pop('sub_category')
			self.fields.pop('keywords') 

	main_category = serializers.StringRelatedField()
	sub_category = serializers.StringRelatedField()
	keywords = serializers.StringRelatedField(many=True)

	class Meta:
		model = Emoji
		fields = ['shortcode', 'codepoint', 'main_category', 'sub_category', 'keywords']


class SubCategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = SubCategory
		fields = ['name']


class MainCategorySerializer(serializers.ModelSerializer):
	subcategories = serializers.StringRelatedField(many=True, source='sub_categories')

	class Meta:
		model = MainCategory
		fields = ['name', 'subcategories']