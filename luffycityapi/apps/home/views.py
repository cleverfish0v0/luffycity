from luffycityapi.utils import constants
from rest_framework.generics import ListAPIView

from .models import Nav
from luffycityapi.apps.home.serializers import NavModelSerializer



class NavHeaderListAPIView(ListAPIView):
    """顶部导航视图"""
    queryset = Nav.objects.filter(position=constants.NAV_HEADER_POSITION, is_show=True, is_deleted=False).order_by("orders", "-id")[:constants.NAV_HEADER_SIZE]
    serializer_class = NavModelSerializer


class NavFooterListAPIView(ListAPIView):
    """脚部导航视图"""
    queryset = Nav.objects.filter(position=constants.NAV_FOOTER_POSITION, is_show=True, is_deleted=False).order_by("orders", "-id")[:constants.NAV_FOOTER_SIZE]
    serializer_class = NavModelSerializer