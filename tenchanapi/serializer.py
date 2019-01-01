from rest_framework import serializers

from .models import Idol, Location, Light, Body, SleepSummary, Sleep, NokiahealthapiToken, Heartrate


class IdolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Idol
        fields = ('name',)
        read_only_fields = ('created_at', 'updated_at')


class SearchLocationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('idol_id', 'timestamp',)
        read_only_fields = ('created_at', 'updated_at')


class LightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Light
        fields = ('timestamp', 'member', 'device', 'sensor', 'light')
        read_only_fields = ('created_at', 'updated_at')


class BodySerializer(serializers.ModelSerializer):
    class Meta:
        model = Body
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at')


class SleepSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = SleepSummary
        fields = ('__all__')
        read_only_fields = ('created_at', 'updated_at')


class SleepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sleep
        fields = ('member', 'startdate', 'enddate', 'sleep_level', 'device')
        read_only_fields = ('created_at', 'updated_at')


class NokiahealthapiTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = NokiahealthapiToken
        fields = ('member', 'access_token', 'refresh_token')
        read_only_fields = ('created_at', 'updated_at')


class HeartrateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Heartrate
        fields = ('timestamp', 'member', 'bpm', 'device')
        read_only_fields = ('created_at', 'updated_at')