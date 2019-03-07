from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from kpop.models import KpopGroups, Members, Songs, GroupCat, Concerts
from kpop.serializers import KpopGroupSerializer, MembersSerializer, SongsSerializer, GroupCatSerializer, ConcertsSerializer
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import filters
# Create your views here.


class GroupCatViewSet(viewsets.ModelViewSet):
    queryset = GroupCat.objects.all()
    serializer_class = GroupCatSerializer


class KpopGroupsViewSet(viewsets.ModelViewSet):
    queryset = KpopGroups.objects.all()
    serializer_class = KpopGroupSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('group_name', 'year_established')


class MembersViewSet(viewsets.ModelViewSet):
    queryset = Members.objects.all()
    serializer_class = MembersSerializer


class SongsViewSet(viewsets.ModelViewSet):
    queryset = Songs.objects.all()
    serializer_class = SongsSerializer


class ConcertsViewSet(viewsets.ModelViewSet):
    queryset = Concerts.objects.all()
    serializer_class = ConcertsSerializer


class GroupMembers(APIView):

    def get(self, request, pk, format=None):
        members = Members.objects.filter(group_name_id=pk)
        serializer = MembersSerializer(members, many=True)
        return Response(serializer.data)


class GroupSongs(APIView):

    def get(self, request, pk, format=None):
        songs = Songs.objects.filter(group_name_id=pk)
        serializer = SongsSerializer(songs, many=True)
        return Response(serializer.data)


class GroupConcerts(APIView):

    def get(self, request, pk, format=None):
        concerts = Concerts.objects.filter(group_name_id=pk)
        serializer = ConcertsSerializer(concerts, many=True)
        return Response(serializer.data)
