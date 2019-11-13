# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Comment(models.Model):
    opinion = models.ForeignKey('Opinion', models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=255)
    created = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'comment'


class Opinion(models.Model):
    topic = models.ForeignKey('Topic', models.DO_NOTHING, blank=True, null=True)
    name = models.TextField()
    color = models.TextField()
    rotation = models.TextField()
    browser = models.CharField(max_length=255)
    platform = models.CharField(max_length=255)
    clientip = models.CharField(db_column='clientIP', max_length=255)  # Field name made lowercase.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    like_opinion = models.IntegerField()
    not_like_opinion = models.IntegerField()
    share_facebook = models.IntegerField()
    share_twitter = models.IntegerField()
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'opinion'


class Topic(models.Model):
    name = models.TextField()
    description = models.TextField(blank=True, null=True)
    url = models.CharField(unique=True, max_length=255)
    acceptcomments = models.IntegerField(db_column='acceptComments')  # Field name made lowercase.
    hashtag = models.TextField()
    maxopinions = models.IntegerField(db_column='maxOpinions')  # Field name made lowercase.
    maxopinionsmobile = models.IntegerField(db_column='maxOpinionsMobile')  # Field name made lowercase.
    treefilekey = models.TextField(db_column='treeFileKey', blank=True, null=True)  # Field name made lowercase.
    backgroundfilekey = models.TextField(db_column='backgroundFileKey', blank=True, null=True)  # Field name made lowercase.
    messagefilekey = models.TextField(db_column='messageFileKey', blank=True, null=True)  # Field name made lowercase.
    filepath = models.TextField(db_column='filePath', blank=True, null=True)  # Field name made lowercase.
    deleted_at = models.DateTimeField(blank=True, null=True)
    share_facebook = models.IntegerField()
    share_twitter = models.IntegerField()
    manual = models.TextField()
    show_in_home = models.BooleanField(default=True)

    class Meta:
        managed = True
        db_table = 'topic'


