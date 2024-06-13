from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import *
from .serializers import *


@csrf_exempt
def album_list(request):
    if request.method == 'GET':
        albums = Album.objects.all()
        album_serializers = AlbumSerializer(albums, many=True)
        return JsonResponse(album_serializers.data, safe=False)


@csrf_exempt
def album_details(request, pk):

    try:
        album = Album.objects.get(id=pk)
    except Album.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        album_serializer = AlbumSerializer(album)
        return JsonResponse(album_serializer.data)


@csrf_exempt
def track_list(request):
    if request.method == 'GET':
        track = Track.objects.all()
        track_serializers = TrackSerializer(track, many=True)
        return JsonResponse(track_serializers.data, safe=False)
