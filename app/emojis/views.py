import json

from django.utils import timezone
from django.db.models import Q
from django.shortcuts import render

from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Emoji, MainCategory, SubCategory, Keyword
from .serializers import EmojiSerializer, MainCategorySerializer


class HelloView(APIView):
	def get(self, request):
		return Response('hello!', status=status.HTTP_200_OK)


class Stats(APIView):
	def get(self, request, format=None):
		response_obj = {
			'date_requested': timezone.localtime(timezone.now()).strftime("%a, %d %b %Y %I:%M:%S"),
			'Total Emojis': Emoji.objects.count(),
			'Recently Added Emojis': Emoji.objects.filter(shortcode__startswith='\u229b').count(),
			'Total Main Categories': MainCategory.objects.count(),
			'Total Sub Categories': SubCategory.objects.count(),
			'Total Keywords': Keyword.objects.count()
		}

		return Response(response_obj, status=status.HTTP_200_OK)


class ListEmojis(ListAPIView):
	queryset = Emoji.objects.all()
	serializer_class = EmojiSerializer

	def filter_queryset(self, queryset):
		queryset = Emoji.objects.all()
		
		# Get main query and build filter if exists
		main_query = self.request.query_params.get('q')
		main_query_filter = Q()

		if main_query:
			main_query_filter = Q(
				Q(shortcode__icontains=main_query) |
				Q(codepoint__icontains=main_query) |
				Q(keywords__name__icontains=main_query)
			)

		# Get main category query and build filter if exists
		main_category = self.request.query_params.get('main_category')
		main_category_filter = Q()

		if main_category:
			main_category_filter = Q(
				Q(main_category__name__icontains=main_category)
			)

		# Get sub category query and build filter if exists
		sub_category = self.request.query_params.get('sub_category')
		sub_category_filter = Q()

		if sub_category:
			sub_category_filter = Q(
				Q(sub_category__name__icontains=sub_category)
			)

		# Get recent boolean query and build filter if exists
		recent = self.request.query_params.get('recent')
		recent_filter = Q()

		if recent in ['True', 'true', 'TRUE']:
			recent_filter = Q(
				shortcode__startswith='\u229b'
			)

		# Combine all filters, order, and distinct
		results = queryset.select_related('main_category', 'sub_category') \
						  .prefetch_related('keywords') \
						  .filter(
							main_query_filter &
							main_category_filter & 
							sub_category_filter &
							recent_filter
						  ) \
						  .order_by('shortcode') \
						  .distinct()
		

		# Get limit if exists
		limit = self.request.query_params.get('limit')
		if limit:
			limit = int(limit)
			return results[:limit]
		else:
			return results

		# # Combine all filters, order, and distinct
		# return (
		# 	queryset
		# 	.select_related('main_category', 'sub_category')
		# 	.prefetch_related('keywords')
		# 	.filter(
		# 		main_query_filter &
		# 		main_category_filter & 
		# 		sub_category_filter &
		# 		recent_filter
		# 	)
		# 	.order_by('shortcode')
		# 	.distinct()
		# )


class ListCategories(ListAPIView):
	queryset = MainCategory.objects.all()
	serializer_class = MainCategorySerializer
