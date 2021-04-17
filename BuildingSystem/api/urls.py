from .views import (
    GetBuildingList,
    BuildingDetail,
    GetRoomList,
    DeviceUpdate,
    BuildingUpdate
)
from django.urls import path

urlpatterns = [
    path('listbuilding/',GetBuildingList.as_view(), name = 'building_list'),    # API get list tòa nhà
    path('detailbuilding/<pk>',BuildingDetail.as_view(),name = 'building_detail'), # Get API thông tin chi tiết của tòa nhà như là mô tả,số phòng
    path('devicebuilding/',GetRoomList.as_view(),name = 'device_list'), # API get thiết bị của từng phòng riêng biệt
    path('deviceupdate/<pk>',DeviceUpdate.as_view(),name='update_device'), #API update device 
    path('buildingupdate/<pk>',BuildingUpdate.as_view(),name='update_building') # API nhập thông tin tòa nhà,thông tin phòng
    ]
