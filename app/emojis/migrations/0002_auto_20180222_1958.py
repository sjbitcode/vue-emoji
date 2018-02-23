# Generated by Django 2.0.2 on 2018-02-22 19:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('emojis', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='emoji',
            name='keywords',
            field=models.ManyToManyField(blank=True, help_text='Emoji Keywords', related_name='emojis', to='emojis.Keyword', verbose_name='Keywords'),
        ),
        migrations.AlterField(
            model_name='emoji',
            name='unicode_version',
            field=models.ForeignKey(blank=True, help_text='Unicode Version', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='emojis', to='emojis.UnicodeVersion', verbose_name='Unicode Version'),
        ),
    ]