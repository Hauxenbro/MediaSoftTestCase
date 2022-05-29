from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

router = DefaultRouter()
router.register('city', CityViewSet, basename='city')
router.register('shop', ShopViewSet, basename='shop')

streets_list = StreetViewSet.as_view({'get':'list'})

urlpatterns = [
    path('<int:city_id>/street/', streets_list, name='streets'),
]
urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += router.urls
