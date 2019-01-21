from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Location, Light, Body, SleepSummary, Sleep, NokiahealthapiToken, Heartrate
from .serializer import SearchLocationsSerializer, LightSerializer, BodySerializer, SleepSummarySerializer, SleepSerializer,\
    NokiahealthapiTokenSerializer, HeartrateSerializer
from .services import culc_observation_range, create_observation_data_list, create_locationsearch, create_observation


class SearchLocationsView(APIView):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        # 古いクライアントではリクエストデータにuuidが付与されていないので、例外処理をする
        try:
            uuid = request.data['uuid']
        except KeyError:
            uuid = None

        create_locationsearch(request.user, request.META['HTTP_USER_AGENT'], uuid)

        latitude = float(request.data['latitude'])
        longitude = float(request.data['longitude'])

        latitude_min, latitude_max, longitude_min, longitude_max = culc_observation_range(latitude, longitude)

        location_obj = Location.objects.filter(
            latitude__gte=latitude_min,
            latitude__lte=latitude_max,
            longitude__gte=longitude_min,
            longitude__lte=longitude_max,
        )
        search_locations_serializers = SearchLocationsSerializer(location_obj, many=True)

        content = {'isFound': False}

        if search_locations_serializers.data != []:
            create_observation(request.user, request.META['HTTP_USER_AGENT'], latitude, longitude, uuid)

            observation_data_list = create_observation_data_list(search_locations_serializers.data)

            content = {
                'isFound': True,
                'data': observation_data_list
            }

        return Response(content, status.HTTP_200_OK)


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