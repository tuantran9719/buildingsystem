from .models import Building,Room,Device
from rest_framework import serializers
from rest_framework.response import Response
from django.db.models import Count
from django.http import JsonResponse



class GetListBuildingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Building
        fields = ["name"]


class BuildingSerializer(serializers.ModelSerializer):
   
    count = serializers.SerializerMethodField()
    rooms = serializers.StringRelatedField(many=True)

    class Meta:
        model = Building
        fields = ("name","address","rooms","count")
    
    def get_count(self,obj):
        from .models import Room,Building
        count_room = Room.objects.filter(building=obj).count()
        return count_room

class DeviceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Device
        fields = ["name" ,"is_active"]
        read_only_fields = ['name']

class RoomSerializer(serializers.ModelSerializer):
    devices = serializers.StringRelatedField(many=True)
    
    class Meta:
        model = Room
        fields = ["building","number","devices"]

    def to_representation(self, instance):
        rep = super(RoomSerializer, self).to_representation(instance)
        rep['building'] = instance.building.name
        return rep

class RoomSerializer1(serializers.ModelSerializer):
    
    class Meta:
        model = Room
        fields = ["number"]
        

class BuildingDetailSerializer(serializers.ModelSerializer):
   
    rooms = RoomSerializer1(many=True)
 
    class Meta:
        model = Building
        fields = [
                "name",
                "address",
                "rooms",
                 ]

    
    


    





