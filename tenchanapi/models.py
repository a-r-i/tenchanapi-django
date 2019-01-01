from django.db import models

class Idol(models.Model):
    idol_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    idolgroup_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Idolgroup(models.Model):
    idolgroup_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Location(models.Model):
    timestamp = models.CharField(max_length=19)
    idol_id = models.IntegerField(null=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class SearchLocation(models.Model):
    timestamp = models.CharField(max_length=19)
    request_user = models.CharField(max_length=100)
    http_user_agent = models.CharField(max_length=100)
    uuid = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Observation(models.Model):
    timestamp = models.IntegerField()
    request_user = models.CharField(max_length=100, null=True)
    http_user_agent = models.CharField(max_length=100, null=True)
    uuid = models.CharField(max_length=100, null=True)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Body(models.Model):
    timestamp = models.IntegerField()
    member = models.IntegerField(null=True)
    muscle_mass = models.IntegerField(null=True)
    hydration = models.IntegerField(null=True)
    bone_mass = models.IntegerField(null=True)
    device = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Heartrate(models.Model):
    timestamp = models.IntegerField()
    member = models.IntegerField(null=True)
    bpm = models.IntegerField()
    device = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)


class Light(models.Model):
    timestamp = models.IntegerField()
    member = models.IntegerField(null=True)
    device = models.CharField(max_length=100, null=True)
    sensor = models.CharField(max_length=100, null=True)
    light = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)


class NokiahealthapiToken(models.Model):
    member = models.IntegerField(null=True)
    access_token = models.TextField()
    refresh_token = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class SleepSummary(models.Model):
    member = models.IntegerField(null=True)
    startdate = models.IntegerField()
    enddate = models.IntegerField()
    wakeupduration = models.IntegerField()
    lightsleepduration = models.IntegerField()
    deepsleepduration = models.IntegerField()
    remsleepduration = models.IntegerField()
    durationtosleep = models.IntegerField()
    durationtowakeup = models.IntegerField()
    wakeupcount = models.IntegerField()
    device = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Sleep(models.Model):
    member = models.IntegerField(null=True)
    sleep_level = models.IntegerField()
    startdate = models.IntegerField(null=True)
    enddate = models.IntegerField(null=True)
    device = models.CharField(max_length=100, null=True)
    registered_at = models.IntegerField(null=True)
    timestamp = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)