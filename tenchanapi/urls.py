from rest_framework import routers
from .views import LightViewSet, BodyViewSet, SleepSummaryViewSet, SleepViewSet, NokiahealthapiTokenViewSet, HeartrateViewSet

router = routers.DefaultRouter()
router.register(r'lights',  LightViewSet)
router.register(r'bodies',  BodyViewSet)
router.register(r'sleepsummaries',  SleepSummaryViewSet)
router.register(r'sleeps',  SleepViewSet)
router.register(r'nokiahealthapi_tokens',  NokiahealthapiTokenViewSet)
router.register(r'heartrates',  HeartrateViewSet)