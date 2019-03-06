from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from kpop.models import KpopGroups, Members, Songs, GroupCat
from kpop.serializers import KpopGroupSerializer, MembersSerializer, SongsSerializer, GroupCatSerializer
from rest_framework.views import APIView
from django.http import Http404
# Create your views here.


class GroupCatViewSet(viewsets.ModelViewSet):
    queryset = GroupCat.objects.all()
    serializer_class = GroupCatSerializer


class KpopGroupsViewSet(viewsets.ModelViewSet):
    queryset = KpopGroups.objects.all()
    serializer_class = KpopGroupSerializer


class MembersViewSet(viewsets.ModelViewSet):
    queryset = Members.objects.all()
    serializer_class = MembersSerializer


class SongsViewSet(viewsets.ModelViewSet):
    queryset = Songs.objects.all()
    serializer_class = SongsSerializer


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
