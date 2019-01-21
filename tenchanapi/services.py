from .models import Idol, SearchLocation, Observation
from .serializer import IdolSerializer

import time


def culc_observation_range(latitude, longitude):
    # 観測通知を出す範囲。ユーザーが、過去のアイドルの位置に、どれくらい近ければ通知を出すか。0.000005=1m。約10m以内に設定。
    RANGE = 0.00005

    latitude_min = latitude - RANGE
    latitude_max = latitude + RANGE
    longitude_min = longitude - RANGE
    longitude_max = longitude + RANGE

    return latitude_min, latitude_max, longitude_min, longitude_max


def create_observation_data_list(search_locations_serialized_data):
    observation_data_list = []
    for d in search_locations_serialized_data:
        idol_obj = Idol.objects.filter(idol_id=d['idol_id'])
        idol_serializers = IdolSerializer(idol_obj, many=True)
        idol_name = idol_serializers.data[0]['name']

        observation_data = {'idol_name': idol_name, 'timestamp': d['timestamp']}
        observation_data_list.append(observation_data)

    return observation_data_list


def create_locationsearch(request_user, http_user_agent, uuid):
    now_unixtime = int(time.time())
    searchlocation = SearchLocation(
                                    timestamp=now_unixtime,
                                    request_user=request_user,
                                    http_user_agent=http_user_agent,
                                    uuid=uuid
                                    )
    searchlocation.save()


def create_observation(request_user, http_user_agent, latitude, longitude, uuid):
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