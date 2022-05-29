from rest_framework import serializers
from .models import Shops, Street, City

class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shops
        fields = ('id', 'title', 'city', 'street', 'house_number', 'open_time', 'close_time')

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        url = serializers.HyperlinkedIdentityField(view_name='city-detail')
        fields = ('id', 'title', 'url')

class StreetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Street
        fields = ('id', 'title', 'city')