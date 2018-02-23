import uuid

from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
	'''
	Base model.
	'''
	id = models.UUIDField(
		db_index=True,
		default=uuid.uuid4,
		editable=False,
		primary_key=True
	)

	created_on = models.DateTimeField(
		auto_now_add=True
	)

	updated_on = models.DateTimeField(
		auto_now=True
	)

	@property
	def id_(self):
		return str(self.id)

	class Meta:
		abstract = True


class Emoji(BaseModel):
	'''
	Emoji Model.
	'''
	codepoint = models.CharField(
		max_length=150,
		verbose_name='UTF-8 Codepoint',
		help_text='This emoji\'s Unicode codepoints'
	)

	shortcode = models.CharField(
		max_length=200,
		verbose_name='Shortcode',
		help_text='This emoji\'s shortcode'
	)

	main_category = models.ForeignKey(
		'MainCategory',
		related_name='emojis',
		verbose_name='Main Category',
		help_text='This emoji\'s main category',
		on_delete=models.SET_NULL,
		blank=True,
		null=True
	)

	sub_category = models.ForeignKey(
		'SubCategory',
		related_name='emojis',
		verbose_name='Sub Category',
		help_text='This emoji\'s sub category',
		on_delete=models.SET_NULL,
		blank=True,
		null=True
	)

	keywords = models.ManyToManyField(
		'Keyword',
		related_name='emojis',
		verbose_name='Keywords',
		help_text='This emoji\'s keywords',
		blank=True
	)

	unicode_version = models.ForeignKey(
		'UnicodeVersion',
		related_name='emojis',
		verbose_name='Unicode Version',
		help_text='This emoji\'s unicode version',
		on_delete=models.CASCADE,
		blank=True,
		null=True
	)

	def __str__(self):
		return self.shortcode


class MainCategory(BaseModel):
	'''
	Main Category Model.
	'''
	name = models.CharField(
		max_length=100,
		verbose_name='Main Category',
		help_text='Main category field for an emoji'
	)

	def __str__(self):
		return self.name


class SubCategory(BaseModel):
	'''
	Sub Category Model.
	'''
	name = models.CharField(
		max_length=100,
		verbose_name='Sub Category',
		help_text='Sub category field for an emoji'
	)

	parent_category= models.ForeignKey(
		'MainCategory',
		related_name='sub_categories',
		verbose_name='Main Parent Category',
		help_text='The main category of this sub category',
		on_delete=models.CASCADE
	)

	def __str__(self):
		return self.name


class UnicodeVersion(BaseModel):
	'''
	Unicode Version model.
	'''
	year = models.PositiveSmallIntegerField(
		verbose_name='Unicode Version Year',
		help_text='Unicode version release year'
	)

	number = models.CharField(
		max_length=10,
		verbose_name='Unicode Version',
		help_text='Unicode version number'
	)

	def __str__(self):
		return 'Unicode {} ({})'.format(self.number, self.year)


class Keyword(BaseModel):
	'''
	Keyword/Tag Model.
	'''
	name = models.CharField(
		max_length=200,
		verbose_name='Emoji Keyword',
		help_text='Keyword for an emoji'
	)

	def __str__(self):
		return self.name
