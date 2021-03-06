# Generated by Django 2.2.1 on 2019-05-30 06:08

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('news', '0003_auto_20190530_1030'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='article_tags',
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
