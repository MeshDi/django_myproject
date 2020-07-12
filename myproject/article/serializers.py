from rest_framework import serializers
from.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'description', 'body', 'author_id')

        def update(self, instance, validated_data):
         instance.author_id = validated_data.get('author_id', instance.author_id)

         instance.save()
         return instance
