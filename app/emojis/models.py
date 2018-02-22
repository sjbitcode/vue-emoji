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
		help_text='Emoji Unicode UTF-8 Representation'
	)

	shortcode = models.CharField(
		max_length=200,
		verbose_name='Shortcode',
		help_text='Emoji Shortcode'
	)

	sub_category = models.ForeignKey(
		'SubCategory',
		related_name='emojis',
		verbose_name='Category',
		help_text='Emoji Category',
		on_delete=models.SET_NULL,
		blank=True,
		null=True
	)

	keywords = models.ManyToManyField(
		'Keyword',
		related_name='emojis',
		verbose_name='Keywords',
		help_text='Emoji Keywords',
		blank=True
	)

	unicode_version = models.ForeignKey(
		'UnicodeVersion',
		related_name='emojis',
		verbose_name='Unicode Version',
		help_text='Unicode Version',
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
		help_text='Main Category Field for an Emoji'
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
		help_text='Sub Category Field for an Emoji'
	)

	parent_category= models.ForeignKey(
		'MainCategory',
		related_name='sub_categories',
		verbose_name='Sub Category',
		help_text='Emoji Sub Category',
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
		help_text='Unicode Version Release Year'
	)

	number = models.CharField(
		max_length=10,
		verbose_name='Unicode Version',
		help_text='Unicode Version Number'
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
		help_text='Keyword Field for an Emoji'
	)

	def __str__(self):
		return self.name
