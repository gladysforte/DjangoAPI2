from kpop.models import KpopGroups, Members, Songs, GroupCat, Concerts
from rest_framework import serializers


class GroupCatSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupCat
        fields = ('id', 'group_category')


class KpopGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = KpopGroups
        # fields = ('id', 'group_name', 'year_established', 'origin',
        #           'website', 'alias', 'group_category')
        fields = '__all__'

class MembersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Members
        fields = ('id', 'fullname', 'bday', 'gender', 'birthplace',
                  'group_name')


class SongsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Songs
        fields = ('id', 'title', 'released_date', 'genre', 'group_name')


class ConcertsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Concerts
        fields = ('id', 'venue', 'country', 'date', 'time', 'group_name')
