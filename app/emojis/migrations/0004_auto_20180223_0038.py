# Generated by Django 2.0.2 on 2018-02-23 00:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('emojis', '0003_auto_20180222_2338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emoji',
            name='sub_category',
            field=models.ForeignKey(blank=True, help_text='Emoji Sub Category', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='emojis', to='emojis.SubCategory', verbose_name='Sub Category'),
        ),
    ]
