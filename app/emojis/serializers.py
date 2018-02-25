from rest_framework import serializers

from .models import Emoji, SubCategory, MainCategory


class EmojiSerializer(serializers.ModelSerializer):
	main_category = serializers.StringRelatedField()
	sub_category = serializers.StringRelatedField()
	keywords = serializers.StringRelatedField(many=True)

	class Meta:
		model = Emoji
		fields = ['codepoint', 'shortcode', 'main_category', 'sub_category', 'keywords']


class SubCategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = SubCategory
		fields = ['name']


class CategorySerializer(serializers.ModelSerializer):
	# subcategories = SubCategorySerializer(many=True, source='sub_categories')
	subcategories = serializers.StringRelatedField(many=True, source='sub_categories')

	class Meta:
		model = MainCategory
		fields = ['name', 'subcategories']