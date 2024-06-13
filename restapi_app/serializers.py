from rest_framework import serializers
from .models import *


class TrackFilterListSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        data = data.filter(length='4.25')
        return super(TrackFilterListSerializer, self).to_representation(data)


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        list_serializer_class = TrackFilterListSerializer
        fields = [
            "id",
            "title",
            "length",
        ]


class AlbumSerializer(serializers.ModelSerializer):
    tracks = TrackSerializer(many=True, read_only=True)

    class Meta:
        model = Album
        fields = [
            "id",
            "title",
            "artist",
            "tracks"
        ]

        

