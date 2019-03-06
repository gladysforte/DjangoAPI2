from kpop.models import KpopGroups, Members, Songs, GroupCat
from rest_framework import serializers


class GroupCatSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupCat
        fields = ('id', 'group_category')


class KpopGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = KpopGroups
        fields = ('id', 'group_name', 'year_established', 'origin',
                  'website', 'alias', 'group_category')


class MembersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Members
        fields = ('id', 'fullname', 'bday', 'gender', 'birthplace',
                  'group_name')


class SongsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Songs
        fields = ('id', 'title', 'released_date', 'genre', 'group_name')
