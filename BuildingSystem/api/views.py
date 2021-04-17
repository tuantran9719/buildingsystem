from django.shortcuts import render
from rest_framework import generics
from .models import Room,Building,Device
from .serializers import GetListBuildingSerializer, RoomSerializer,BuildingSerializer,DeviceSerializer,BuildingDetailSerializer
from rest_framework.response import Response
from django.db.models import Count



class GetBuildingList(generics.ListAPIView):
    queryset = Building.objects.all()
    serializer_class = GetListBuildingSerializer
   
    def list(self, request):
        queryset = self.get_queryset()
        serializer = GetListBuildingSerializer(queryset, many = True)
        return Response(serializer.data)

class GetRoomList(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = RoomSerializer(queryset,many=True)
        return Response(serializer.data)

class BuildingDetail(generics.RetrieveAPIView):
    queryset  = Building.objects.all()
    serializer_class = BuildingSerializer

class DeviceUpdate(generics.RetrieveUpdateAPIView):
    queryset = Device.objects.all()
    serializer_class= DeviceSerializer

class BuildingUpdate(generics.RetrieveUpdateAPIView):
    queryset = Building.objects.all()
    serializer_class = BuildingDetailSerializer




    
    

    

