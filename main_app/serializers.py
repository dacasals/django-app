from rest_framework import serializers
from social_core.utils import build_absolute_uri

from main_app.models import Topic


class TreeSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=False, max_length=250)
    description = serializers.CharField(required=True, max_length=250)
    url = serializers.CharField(required=True, max_length=250)
    hashtag = serializers.CharField(required=True,  max_length=250)
    share_facebook = serializers.IntegerField(required=True)
    share_twitter = serializers.IntegerField(required=True)

    class Meta:
        model = Topic
        fields = ['id', 'name', 'description', 'url', 'hashtag', 'share_facebook', 'share_twitter']
