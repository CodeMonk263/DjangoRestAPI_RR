from rest_framework import serializers

from data.models import Data

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model=Data
        fields = [
            'userId',
            'id',
            'title',
            'body'
        ]

        read_only_fields = ['userId','id']

    def validate(self, data):
        title = data.get("title", None)
        if (len(title)==0):
            raise serializers.ValidationError("Title cannot be empty")
        return data