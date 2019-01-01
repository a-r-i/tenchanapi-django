from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Idol, Location, SearchLocation, Observation, Light, Body, SleepSummary, Sleep, NokiahealthapiToken, Heartrate
from .serializer import IdolSerializer, SearchLocationsSerializer, LightSerializer, BodySerializer,\
                        SleepSummarySerializer, SleepSerializer, NokiahealthapiTokenSerializer, HeartrateSerializer

import time

class SearchLocations(APIView):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        try:
            uuid = request.data['uuid']
        except KeyError:
            uuid = None

        self.create_locationsearch(request.user, request.META['HTTP_USER_AGENT'], uuid)

        latitude = float(request.data['latitude'])
        longitude = float(request.data['longitude'])

        # 観測通知を出す範囲。ユーザーが、過去の・ちゃんの位置に、どれくらい近ければ通知を出すか。0.000005=1m。約10m以内に設定。
        RANGE = 0.00005

        latitude_min = latitude - RANGE
        latitude_max = latitude + RANGE
        longitude_min = longitude - RANGE
        longitude_max = longitude + RANGE

        location_obj = Location.objects.filter(
                                      latitude__gte=latitude_min,
                                      latitude__lte=latitude_max,
                                      longitude__gte=longitude_min,
                                      longitude__lte=longitude_max,
                                      )
        search_locations_serializers = SearchLocationsSerializer(location_obj, many=True)

        if search_locations_serializers.data == []:
            content = {'isFound': False }
        else:
            self.create_observation(request.user, request.META['HTTP_USER_AGENT'], latitude, longitude, uuid)

            data_array = []
            for d in search_locations_serializers.data:
                idol_obj = Idol.objects.filter(idol_id=d['idol_id'])
                idol_serializers = IdolSerializer(idol_obj, many=True)
                idol_name = idol_serializers.data[0]['name']

                data = {'idol_name':idol_name, 'timestamp':d['timestamp']}
                data_array.append(data)

            content = {
                        'isFound': True,
                        'data': data_array
                        }

        return Response(content, status.HTTP_200_OK)

    def create_locationsearch(self, request_user, http_user_agent, uuid):
        now_unixtime = int(time.time())
        searchlocation = SearchLocation(
                                        timestamp=now_unixtime,
                                        request_user=request_user,
                                        http_user_agent=http_user_agent,
                                        uuid=uuid
                                        )
        searchlocation.save()

    def create_observation(self, request_user, http_user_agent, latitude, longitude, uuid):
        now_unixtime = int(time.time())
        observation = Observation(
                                    timestamp=now_unixtime,
                                    request_user=request_user,
                                    http_user_agent=http_user_agent,
                                    uuid=uuid,
                                    latitude=latitude,
                                    longitude=longitude
                                 )
        observation.save()


class LightViewSet(viewsets.ModelViewSet):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = Light.objects.all()
    serializer_class = LightSerializer
    

class BodyViewSet(viewsets.ModelViewSet):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = Body.objects.all()
    serializer_class = BodySerializer


class SleepSummaryViewSet(viewsets.ModelViewSet):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = SleepSummary.objects.all()
    serializer_class = SleepSummarySerializer


class SleepViewSet(viewsets.ModelViewSet):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = Sleep.objects.all()
    serializer_class = SleepSerializer


class NokiahealthapiTokenViewSet(viewsets.ModelViewSet):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = NokiahealthapiToken.objects.all()
    serializer_class = NokiahealthapiTokenSerializer


class HeartrateViewSet(viewsets.ModelViewSet):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = Heartrate.objects.all()
    serializer_class = HeartrateSerializer