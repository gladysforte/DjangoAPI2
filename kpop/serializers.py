from kpop.models import KpopGroups, Members, Songs, GroupCat, Concerts
from rest_framework import serializers


class GroupCatSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupCat
        fields = ('id', 'group_category')


class MembersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Members
        fields = ('id', 'fullname', 'bday', 'gender', 'birthplace',
                  'group_name')


class KpopGroupSerializer(serializers.ModelSerializer):
    #members = MembersSerializer(many=True, read_only=True)
    # group_name = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    members = serializers.SerializerMethodField()

    class Meta:
        model = KpopGroups
        fields = ('id', 'group_name', 'year_established', 'origin',
                  'website', 'alias', 'group_category', 'members')
        # fields = '__all__'


    def get_members(self, obj):
        members = Members.objects.filter(group_name_id=obj.id)
        serializer = MembersSerializer(members, many=True)
        return serializer.data


class SongsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Songs
        fields = ('id', 'title', 'released_date', 'genre', 'group_name')


class ConcertsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Concerts
        fields = ('id', 'venue', 'country', 'date', 'time', 'group_name')
