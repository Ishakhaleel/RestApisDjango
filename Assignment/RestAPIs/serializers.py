
from rest_framework import serializers
from .models import User, Advisor


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class AdvisorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advisor
        fields = ['name', 'photo_url', 'advisor_id']


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advisor
        fields = ['name', 'photo_url', 'advisor_id', 'booking_time', 'booking_id']

