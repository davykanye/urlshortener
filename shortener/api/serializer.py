from rest_framework import serializers
from shortener.models import ShortUrl

class ShortSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=65, min_length=8)
    url = serializers.URLField(max_length=200, min_length=None, allow_blank=False)

    class Meta:
        model = ShortUrl
        fields = '__all__'

    def validate(self, attrs):
        return super().validate(attrs)

    def create(self, validated_data):
        return ShortUrl.objects.create(**validated_data)