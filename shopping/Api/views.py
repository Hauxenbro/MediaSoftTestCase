from django.shortcuts import render
from django.utils import timezone
from django.db.models import Q
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import ShopSerializer, CitySerializer, StreetSerializer
from .models import City, Shops, Street

# Create your views here.
Time_now = timezone.now()

class CustomFilter(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        open = request.GET.get('open', None)
        try:
            open = int(open)
            if int(open) == 1:
                return queryset.filter(open_time__lt=Time_now, close_time__gt=Time_now)
            elif int(open) == 0:
                return queryset.filter(Q(open_time__gt=Time_now) | Q(close_time__lt=Time_now))
            else:
                return queryset.all()
        except ValueError:
            return queryset.all()

class CityViewSet(ModelViewSet):
    http_method_names = ['get']
    queryset = City.objects.all()
    serializer_class = CitySerializer

class ShopViewSet(ModelViewSet):
    '''
    api/shop/?street=&city=/
    '''

    queryset = Shops.objects.all()
    filter_backends = (DjangoFilterBackend, CustomFilter)
    filterset_fields = ('street', 'city')
    serializer_class = ShopSerializer

class StreetViewSet(ModelViewSet):
    http_method_names = ['get']
    queryset = Street.objects.all()
    serializer_class = StreetSerializer

    def get_queryset(self):
        city_id = self.kwargs.get('city_id', '')
        query = super().get_queryset()
        return query.filter(city_id = city_id)