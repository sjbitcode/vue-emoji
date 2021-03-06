# Generated by Django 2.0.2 on 2018-02-22 23:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('emojis', '0002_auto_20180222_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategory',
            name='parent_category',
            field=models.ForeignKey(help_text='Emoji Sub Category', on_delete=django.db.models.deletion.CASCADE, related_name='sub_categories', to='emojis.MainCategory', verbose_name='Main Parent Category'),
        ),
    ]
